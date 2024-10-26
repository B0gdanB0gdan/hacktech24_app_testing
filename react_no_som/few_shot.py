example6 = {
    "user": {
        "text": "Query: Click on  \"Media\" button.",
        "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\react\examples\example2\example_vlc.png"
    },
    "steps": 2,
    "assistant": {
        "step1": {
            "text": """
                Thought: I need to find the \"Media\" button coordinates to click on it.
                Action: Click
                Input: 36, 68
                Observation: The dropdown menu appeared.
            """,
            "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\react\examples\example2\image.png"
        },
        "step2": {
            "text": """
                Thought: The button has been pressed.
                Action: Finish
            """,
            "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\data\part_of_screen_word_less2\image.png"
        }
    }
}

example5 = {
    "user": {
        "text": "Query: Click on  \"Print\" button.",
        "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\data\part_of_screen_word_less2\00281.jpg"
    },
    "steps": 2,
    "assistant": {
        "step1": {
            "text": """
                Thought: I need to find the \"Print\" button coordinates to click on it.
                Action: Click
                Input: 65, 454
                Observation: The print menu appeared.
            """,
            "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\data\part_of_screen_word_less2\00281.jpg"
        },
        "step2": {
            "text": """
                Thought: I reached the final frame.
                Action: Finish
            """,
            "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\data\part_of_screen_word_less2\00321.jpg"
        }
    }
}

example4 = {
    "user": {
        "text": "Query: Click on  \"File\" button.",
        "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\data\part_of_screen_word_less2\00201.jpg"
    },
    "steps": 2,
    "assistant": {
        "step1": {
            "text": """
                Thought: I need to find the \"File\" button coordinates to click on it.
                Action: Click
                Input: 63, 98
                Observation: The options menu appeared.
            """,
            "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\data\part_of_screen_word_less2\00201.jpg"
        },
        "step2": {
            "text": """
                Thought: I reached the final frame.
                Action: Finish
            """,
            "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\data\part_of_screen_word_less2\00221.jpg"
        }
    }
}

example3 = {
    "user": {
        "text": "Query: Write \"Hello world!\"",
        "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\data\part_of_screen_word_less2\00001.jpg"
    },
    "steps": 2,
    "assistant": {
        "step1": {
            "text": """
                Thought: First I need to type in the window the text \"Hello world\".
                Action: Type
                Input: Hello world!
                Observation: The text is visible on the page.
            """,
            "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\data\part_of_screen_word_less2\00001.jpg"
        },
        "step2": {
            "text": """
                Thought: I reached the final frame.
                Action: Finish
            """,
            "image_path": r"C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\data\part_of_screen_word_less2\00121.jpg"
        }
    }
}


example2 = {
    "user": {
        "text": "Query: Save a new file called \"myfile.txt\" in Notepad application with content \"Hello world!\"",
        "image_path": "examples/example2/starting_point.png"
    },
    "steps": 5,
    "assistant": {
        "step1": {
            "text": """
                Thought: First I need to type in the window the text \"Hello world\".
                Action: Type
                Input: Hello world!
                Observation: The text is visible on the page.
            """,
            "image_path": "examples/example2/starting_point.png"
        },
        "step2": {
            "text": """     
                Thought: Then I need to find the "File" button's coordinates to open a menu where I would see the save button.
                Action: Click
                Input: 441, 151
                Observation: 
            """,
            "image_path": "examples/example2/step1.png"
        },
        "step3": {
            "text": """
                Thought: Now I see the "Save as..." button. I have to find its coordinates.
                Action: Click
                Input: 557, 277
                Observation:     
            """,
            "image_path": "examples/example2/step2.png"
        },
        "step4": {
            "text": """
                Thought: Next I need to type in the name of the file \"myfile.txt\" I want to save the content to.
                Action: Type
                Input: myfile.txt
                Observation: The text 'myfile.txt' appears in the designated area.
            """,
            "image_path": "examples/example2/step4.png"
        },
        "step5": {
            "text": """
                Thought: Then I can click the save button to save the file with mentioned name and content. 
                Action: Click
                Input: 1174, 724
                Observation:     
            """,
            "image_path": "examples/example2/step5.png"
        },
        "step6": {
            "text": """
                Thought: I reached the final frame.
                Action: Finish
            """,
            "image_path": "examples/example2/step5.png"
        }
    }
}

# example2 = {
#     "user": {
#         "text": "Query: Save a new file called \"myfile.txt\" in Notepad application with content \"Hello world!\"",
#         "image_path": "examples/example2/starting_point.png"
#     },
#     "steps": 5,
#     "assistant": {
#         "step1": {
#             "text": """
#                 Thought: First I need to type in the window the text \"Hello world\".
#                 Action: Type
#                 Input: Hello world!
#                 Observation: 
#             """,
#             "image_path": "examples/example2/starting_point.png"
#         },
#         "step2": {
#             "text": """     
#                 Thought: Then I need to find the "File" button's coordinates to open a menu where I would see the save button.
#                 Action: Click
#                 Input: 441, 151
#                 Observation:     
#             """,
#             "image_path": "examples/example2/step1.png"
#         },
#         "step3": {
#             "text": """
#                 Thought: Now I see the "Save as..." button. I have to find its coordinates.
#                 Action: Click
#                 Input: 557, 277
#                 Observation:     
#             """,
#             "image_path": "examples/example2/step2.png"
#         },
#         "step4": {
#             "text": """
#                 Thought: Next I need to type in the name of the file \"myfile.txt\" I want to save the content to.
#                 Action: Type
#                 Input: myfile.txt
#                 Observation:     
#             """,
#             "image_path": "examples/example2/step4.png"
#         },
#         "step5": {
#             "text": """
#                 Thought: Then I can click the save button to save the file with mentioned name and content. 
#                 Action: Click
#                 Input: 1174, 724
#                 Observation:     
#             """,
#             "image_path": "examples/example2/step5.png"
#         },
#         "step6": {
#             "text": """
#                 Thought: I reached the final frame.
#                 Action: Finish
#             """,
#             "image_path": "examples/example2/step5.png"
#         }
#     }
# }

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
#             "image_path": "examples/example2/step1.png"
#         },
#         "step2": {
#             "text": """
#                 Thought: I need to find the coordinates of the "Search" button.
#                 Action: Click
#                 Input: (600, 700)
#                 Observation:     
#             """,
#             "image_path": "examples/example2/step2.png"
#         },
#         "step3": {
#             "text": """
#                 Thought: I need to find the coordinates of the "Search" button.
#                 Action: Click
#                 Input: (600, 700)
#                 Observation:     
#             """,
#             "image_path": "examples/example2/step3.png"
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
    return [example2,example3, example4,example5, example6]