from core.verdandi import handle_query
from core.logger import save_log
from core.urd import analyze_logs

question = input("Ask Verdandi: ")

response=handle_query(question)
print("\nAnswer:\n")
print(response)

difficulty = input("\nDifficulty (1-5): ")
confusion = input("What confused you : ")

save_log(question, difficulty, confusion)

print("\nSaved.\n")

print("\nUrd Analysis (Weak Topics):\n")
print(analyze_logs())