example1 = {
    "user": {
        "text": "Query: Save a new file called \"myfile.txt\" in Notepad application with content \"Hello world!\"",
        "image_path": "examples/example1/starting_point.png"
    },
    "steps": 5,
    "assistant": {
        "step1": {
            "text": """
                Thought: First I need to find a text area to write text in. Label is 1 resembles a text area. Next I need to type in the window the text \"Hello world\". 
                Label: 1
                Action: Type
                Input: Hello world!
                Observation: 
            """,
            "image_path": "examples/example1/step1.png"
        },
        "step2": {
            "text": """
                Thought: Then I need to prepare for saving. To do that I need to go to \"File\" item in menu. The closest label for the \"File\" element is 12.
                Label: 12
                Action: Click
                Input: None
                Observation:     
            """,
            "image_path": "examples/example1/step2.png"
        },
        "step3": {
            "text": """
                Thought: I can see aslo the \"Save as...\" button. The closest label is 5.
                Label: 5
                Action: Click
                Input: None
                Observation:     
            """,
            "image_path": "examples/example1/step3.png"
        },
        "step4": {
            "text": """
                Thought: Next I need to type in the name of the file \"myfile.txt\" I want to save the content to. The element I'm looking for has label 6.
                Label: 6
                Action: Type
                Input: myfile.txt
                Observation:     
            """,
            "image_path": "examples/example1/step4.png"
        },
        "step5": {
            "text": """
                Thought: I reached the final frame as I see the file name has changed correctly.
                Action: Finish
            """
        }
    }
}

example2 = {
    "user": {
        "text": "Query: Search for keyword \"dogs\" in opened Chrome window",
        "image_path": "examples/example2/starting_point.png"
    },
    "steps": 3,
    "assistant": {
        "step1": {
            "text": """
                Thought: Based on what I see I can directly type \"dogs\" in the search bar. 
                Label: 3
                Action: Type
                Input: dogs
                Observation: 
            """,
            "image_path": "examples/example2/step1.png"
        },
        "step2": {
            "text": """
                Thought: Then I can safely press the suggested option with label 7.
                Label: 7
                Action: Click
                Input: None
                Observation:     
            """,
            "image_path": "examples/example2/step2.png"
        },
        "step3": {
            "text": """
                Thought: I reached the final frame where I can see dogs.
                Action: Finish
            """
        }
    }
}



def get_examples():
    return [example1, example2]