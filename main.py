from config.settings import configure_environment
from interface.gradio_interface import InterfaceBuilder

def main():
    # Configure environment variables
    configure_environment()
    
    # Build and launch interface
    interface = InterfaceBuilder().build()
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )

if __name__ == "__main__":
    main()