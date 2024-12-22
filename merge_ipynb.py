import nbformat

def merge_notebooks(notebook1_path, notebook2_path, output_path):
    # Load the first notebook
    with open(notebook1_path, 'r', encoding='utf-8') as f:
        notebook1 = nbformat.read(f, as_version=4)

    # Load the second notebook
    with open(notebook2_path, 'r', encoding='utf-8') as f:
        notebook2 = nbformat.read(f, as_version=4)

    # Combine the cells of both notebooks
    merged_notebook = nbformat.v4.new_notebook()
    merged_notebook.cells = notebook1.cells + notebook2.cells

    # Save the merged notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(merged_notebook, f)

    print(f"Notebooks merged successfully into {output_path}")

# Paths to your input notebooks and output file
notebook1 = r"C:\Users\prabh\Dropbox\PC\Downloads\05_QA_System_with___LlamaIndex__and_Google_Gemini!(LlamaIndex,_Gemini_Embedding,_GeminiPro.ipynb"
notebook2 = "main.ipynb"  # Adjust this to the correct second notebook path
output_notebook = "my_first_QA_chatApp.ipynb"

# Call the function to merge notebooks
merge_notebooks(notebook1, notebook2, output_notebook)
