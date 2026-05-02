from app.tools.calculator import calculate


def execute_tool(tool_name, arguments):
    if tool_name == "calculate":
        return calculate(arguments)

    return "Tool not found"