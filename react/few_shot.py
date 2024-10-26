example1 = {
    "user": {
        "text": "Query: Save a new file called \"myfile.txt\" in Notepad application with content \"Hello world!\"",
        "image_path": "examples/example1/starting_point.png"
    },
    "steps": 5,
    "assistant": {
        "step1": {
            "text": """
                Thought: First I need to type in the window the text \"Hello world\".
                Action: Type
                Input: Hello world!
                Observation: 
            """,
            "image_path": "examples/example1/step1.png"
        },
        "step2": {
            "text": """
                Thought: Then I need to find the \"File\" button to open a menu where I would see the save button. I see its label is 129.
                Action: Click
                Input: 129
                Observation:     
            """,
            "image_path": "examples/example1/step2.png"
        },
        "step3": {
            "text": """
                Thought: Now I see the \"Save as...\" button with its label 11.
                Action: Click
                Input: 11
                Observation:     
            """,
            "image_path": "examples/example1/step3.png"
        },
        "step4": {
            "text": """
                Thought: Next I need to type in the name of the file \"myfile.txt\" I want to save the content to.
                Action: Type
                Input: myfile.txt
                Observation:     
            """,
            "image_path": "examples/example1/step4.png"
        },
        "step5": {
            "text": """
                Thought: Then I can click the save button to save the file with mentioned name and content. Its label is 46.
                Action: Click
                Input: 46
                Observation:     
            """,
            "image_path": "examples/example1/step5.png"
        },
        "step6": {
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