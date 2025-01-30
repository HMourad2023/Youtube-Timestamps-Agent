import os
import gradio as gr
from typing import Optional
from agents.timestamp_agent import create_youtube_agent

class InterfaceBuilder:
    def __init__(self):
        self.agent = create_youtube_agent()
        self.css = self._load_css()

    def _load_css(self) -> str:
        css_path = os.path.join(
            os.path.dirname(__file__),
            "assets",
            "styles.css"
            )
    
        # Create assets directory if not exists
        os.makedirs(os.path.dirname(css_path), exist_ok=True)
        
        # Create default CSS if missing
        if not os.path.exists(css_path):
            default_css = """/* Default styles */
            .gradio-container { padding: 20px; }"""
            with open(css_path, "w") as f:
                f.write(default_css)
            
            with open(css_path, "r") as f:
                return f.read()

    def _process_input(self, youtube_url: str) -> str:
        if not youtube_url.strip():
            return "⚠️ Please enter a valid YouTube URL"
        
        response = self.agent.run(
            f"Generate comprehensive timestamps for: {youtube_url}"
        )
        return response.content or "❌ No timestamps generated. Please verify the video URL."

    def build(self) -> gr.Blocks:
        with gr.Blocks(css=self.css, title="YouTube Chapter Generator") as demo:
            gr.Markdown("# 🎥 YouTube Chapter Generator")
            gr.Markdown("Automatically create detailed video chapters from any YouTube URL")
            
            with gr.Row():
                url_input = gr.Textbox(
                    label="YouTube Video URL",
                    placeholder="https://youtube.com/watch?v=...",
                    max_lines=1,
                    elem_classes=["input-box"]
                )
                
            with gr.Row():
                submit_btn = gr.Button("Generate Chapters", elem_classes=["primary-btn"])
                
            with gr.Row():
                output = gr.JSON(
                    label="Video Chapters",
                    elem_classes=["output-box"]
                )

            submit_btn.click(
                fn=self._process_input,
                inputs=url_input,
                outputs=output
            )

        return demo