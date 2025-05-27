import sys
import argparse
from http import server

from onnx_vl import OnnxVL
from server import MoondreamHandler


def main():
    parser = argparse.ArgumentParser(description="Moondream CLI")

    # Server command
    parser.add_argument("--model",
                        type=str,
                        default="models/moondream-2b-int8.mf",
                        help="Path to the model file"
                        )
    parser.add_argument("--host",
                        type=str,
                        default="localhost",
                        help="Host to bind to"
                        )
    parser.add_argument("--port",
                        type=int,
                        default=3475,
                        help="Port to listen on"
                        )

    args = parser.parse_args()

    if args.model:
        model = OnnxVL.from_path(args.model)
    else:
        parser.error("Model path is required")

    MoondreamHandler.model = model
    server_address = (args.host, args.port)
    try:
        httpd = server.HTTPServer(server_address, MoondreamHandler)
        print(f"Starting Moondream server on http://{args.host}:{args.port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
