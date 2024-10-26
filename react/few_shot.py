example1 = {
    "user": "Query: Type \"dogs\" in the Chrome search bar.",
    "steps": 3,
    "assistant": {
        "step1": {
            "text": """
                Thought: First I need to find the coordinates of the Chrome icon.
                Action: Click
                Input: (900, 1070)
                Observation: 
            """,
            "image_path": "examples/example1/step1.png"
        },
        "step2": {
            "text": """
                Thought: Then I need to type in the word \"dogs\".
                Action: Type
                Input: dogs
                Observation:     
            """,
            "image_path": "examples/example1/step2.png"
        },
        "step3": {
            "text": """
                Thought: I reached the final frame.
                Action: Finish
            """
        }
    }
}

# example2 = {
#     "user": "Query: Click on the \"Search\" button located at the bottom right corner.",
#     "steps": 4,
#     "assistant": {
#         "step1": {
#             "text": """
#                 Thought: I need to find the coordinates of the "Search" button.
#                 Action: Click
#                 Input: (600, 700)
#                 Observation: 
#             """,
#             "image_path": "examples/example1/step1.png"
#         },
#         "step2": {
#             "text": """
#                 Thought: I need to find the coordinates of the "Search" button.
#                 Action: Click
#                 Input: (600, 700)
#                 Observation:     
#             """,
#             "image_path": "examples/example1/step2.png"
#         },
#         "step3": {
#             "text": """
#                 Thought: I need to find the coordinates of the "Search" button.
#                 Action: Click
#                 Input: (600, 700)
#                 Observation:     
#             """,
#             "image_path": "examples/example1/step3.png"
#         },
#         "step4": {
#             "text": """
#                 Thought: I reached the final frame.
#                 Action: Finish
#             """
#         }
#     }
# }

def get_examples():
    return [example1]