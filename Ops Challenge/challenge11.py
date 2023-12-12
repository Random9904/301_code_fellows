# Python Requests Library
import requests

def translate_status_code(code):
    status_codes = {
        100: 'Continue',
        101: 'Switching Protocols',
        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        203: 'Non-Authoritative Information',
        204: 'No Content',
        205: 'Reset Content',
        206: 'Partial Content',
        300: 'Multiple Choices',
        301: 'Moved Permanently',
        302: 'Found',
        303: 'See Other',
        304: 'Not Modified',
        305: 'Use Proxy',
        307: 'Temporary Redirect',
        400: 'Bad Request',
        401: 'Unauthorized',
        402: 'Payment Required',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        406: 'Not Acceptable',
        407: 'Proxy Authentication Required',
        408: 'Request Timeout',
        409: 'Conflict',
        410: 'Gone',
        411: 'Length Required',
        412: 'Precondition Failed',
        413: 'Request Entity Too Large',
        414: 'Request-URI Too Long',
        415: 'Unsupported Media Type',
        416: 'Requested Range Not Satisfiable',
        417: 'Expectation Failed',
        500: 'Internal Server Error',
        501: 'Not Implemented',
        502: 'Bad Gateway',
        503: 'Service Unavailable',
        504: 'Gateway Timeout',
        505: 'HTTP Version Not Supported'
    }

    return status_codes.get(code, 'Unknown Status Code')

def main():
    # Prompt the user to type a string input as the variable for your destination URL
    destination_input = input("Enter the destination URL (example: google.com): ")

    # Add "http://" if not already present
    destination_url = destination_input if "://" in destination_input else f"http://{destination_input}"

    # Prompt the user to select a HTTP Method
    # .upper() -> converts all text into UPPERCASE
    http_method = input("Choose HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

    # Print to the screen the entire request your script is about to send
    print(f"\nSending {http_method} request to: {destination_url}")

    # Ask the user to confirm before proceeding
    # .lower() -> all text into lowercase
    confirm = input("Do you want to proceed? (y/n): ").lower()
    # return exits function
    if confirm != 'y':
        print("Request canceled.")
        return

    # Using the requests library, perform a request against the destination URL 
    # with the HTTP Method selected by the user
    response = requests.request(http_method, destination_url)

    # For the given header, translate the codes into plain 
    # terms that print to the screen
    print(f"\nStatus Code: {response.status_code} - {translate_status_code(response.status_code)}")

    # For the given URL, print response header information to the screen
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

# Run main function 
# ---- Script starts here -----
main()