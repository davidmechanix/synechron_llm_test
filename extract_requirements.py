import json
import os

def read_regulations(file_path):
    """Read the regulatory text file and return its content."""
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []

def segment_text(lines):
    """Segment the text into sections."""
    sections = []
    section = []

    for line in lines:
        if line.strip():
            section.append(line.strip())
        else:
            if section:
                sections.append(" ".join(section))
                section = []

    if section:
        sections.append(" ".join(section))

    return sections

def simulate_llm_summary(text_section):
    """Simulate LLM summarization by reversing words in the section."""
    words = text_section.split()
    return " ".join(reversed(words))

def extract_requirements(sections):
    """Extract summaries and store them in a structured format."""
    extracted = []

    for i, section in enumerate(sections, 1):
        summary = simulate_llm_summary(section)
        extracted.append({
            "section_number": i,
            "original_text": section,
            "summary": summary
        })

    return extracted

def save_output(extracted_data, output_file):
    """Save extracted summaries to a JSON file."""
    try:
        with open(output_file, 'w') as file:
            json.dump(extracted_data, file, indent=4)
        print(f"Output successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving output: {e}")

if __name__ == "__main__":
    # Input file path
    input_file = "regulations.txt"

    # Output file path
    output_file = "extracted_requirements.json"

    # Read regulatory text file
    lines = read_regulations(input_file)
    if not lines:
        exit(1)

    # Segment the text
    sections = segment_text(lines)

    # Extract requirements
    extracted_data = extract_requirements(sections)

    # Save output
    save_output(extracted_data, output_file)
