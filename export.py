# Export functions

def export_answers(a_text, answer):
    file_ = open("reports.txt", "a+")
    file_.write(str(a_text)+ "\n")
    file_.write(str(answer) + "\n\n")
    file_.close()
