example1 = {
"user": "Query: Click on the \"Search\" button located at the bottom right corner.",
"assistant": """
Thought: I need to find the coordinates of the "Search" button.
Action: Click
Input: (600, 700)
Observation: 
"""
}

example2 = {
"user": "Query: Type \"Hello World\" after clicking at coordinates (100, 200)",   
"assistant": """
Thought: I need to click on (100, 200) and then type the provided text.
Action: Click
Input: (100, 200)
Observation: 
"""
}

example3 = {
"user": "Query: Scroll up by 3 pages.",
"assistant": """
Thought: Scrolling up by 3 pages requires a scroll command.
Action: Scroll
Input: 300
Observation: 
"""
}

example4 = {
"user": "Query: Move the cursor to the center of the screen.",
"assistant": """
Thought: I should move the cursor to the center coordinates.
Action: MoveCursor
Input: (960, 540)
Observation: 
"""
}

examples = [example1, example2, example3, example4]