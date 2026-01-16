"""
AI Description Generator

Generates descriptions for functions, methods, and endpoints using AI.
"""

from typing import Dict, Optional


def generate_function_description(
    func_name: str,
    params: str,
    returns: str,
    receiver: Optional[str] = None,
    file_path: Optional[str] = None
) -> str:
    """
    Generate a description for a function using AI.
    
    Args:
        func_name: Name of the function
        params: Function parameters
        returns: Return type
        receiver: Optional receiver (for methods)
        file_path: Optional file path for context
    
    Returns:
        Generated description text
    """
    # TODO: Replace with actual AI API call
    # For now, return a demo description based on function signature
    
    # Build function signature context
    sig_parts = []
    if receiver:
        sig_parts.append(f"method {func_name}")
    else:
        sig_parts.append(f"function {func_name}")
    
    if params:
        sig_parts.append(f"with parameters: {params}")
    
    if returns:
        sig_parts.append(f"returning {returns}")
    
    # Generate demo description
    description = f"{func_name} is a "
    if receiver:
        description += "method that "
    else:
        description += "function that "
    
    # Try to infer purpose from name
    if func_name.startswith('Get') or func_name.startswith('Fetch'):
        description += "retrieves data"
    elif func_name.startswith('Set') or func_name.startswith('Update'):
        description += "updates data"
    elif func_name.startswith('Create') or func_name.startswith('Add'):
        description += "creates new data"
    elif func_name.startswith('Delete') or func_name.startswith('Remove'):
        description += "deletes data"
    elif func_name.startswith('List') or func_name.startswith('Find'):
        description += "lists or finds data"
    elif func_name.startswith('Handle') or func_name.startswith('Process'):
        description += "handles or processes requests"
    else:
        description += "performs operations"
    
    if params:
        description += f" based on the provided parameters"
    
    if returns:
        if 'error' in returns.lower():
            description += " and may return an error"
        elif returns:
            description += f" and returns {returns}"
    
    description += "."
    
    return description


def generate_endpoint_description(
    method: str,
    path: Optional[str] = None,
    handler: Optional[str] = None,
    request_type: Optional[str] = None,
    response_type: Optional[str] = None
) -> str:
    """
    Generate a description for an API endpoint using AI.
    
    Args:
        method: HTTP method (GET, POST, etc.) or gRPC method name
        path: Optional REST path
        handler: Optional handler function name
        request_type: Optional request type
        response_type: Optional response type
    
    Returns:
        Generated description text
    """
    # TODO: Replace with actual AI API call
    # For now, return a demo description
    
    if path:
        # REST endpoint
        description = f"{method} {path} endpoint"
        if handler:
            description += f" handled by {handler}"
        description += "."
        
        if method == 'GET':
            description += " Retrieves data from the server."
        elif method == 'POST':
            description += " Creates new resources."
        elif method == 'PUT':
            description += " Updates existing resources."
        elif method == 'DELETE':
            description += " Deletes resources."
        elif method == 'PATCH':
            description += " Partially updates resources."
        
        if request_type:
            description += f" Accepts {request_type} as request body."
        if response_type:
            description += f" Returns {response_type} as response."
    else:
        # gRPC endpoint
        description = f"{method} is a gRPC method"
        if request_type:
            description += f" that accepts {request_type}"
        if response_type:
            description += f" and returns {response_type}"
        description += "."
    
    return description
