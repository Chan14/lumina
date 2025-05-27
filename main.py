from core.goals import add_goal, list_goals
from core.journal import add_note, show_notes

# from core.review import generate_study_review
from core.review import generate_study_review_gemini


def _print_menu():
    print("✨ Lumina: Your Learning Companion ✨")
    print("1. Add a learning note")
    print("2. Show all notes")
    print("3. Add a long-term goal")
    print("4. Show goals")
    print("5. Get AI study review")
    print("6. Exit")


def get_sub_prompt_from_console():
    print(
        "Please enter any additional context or questions for Lumina (press Enter to skip):"
    )
    return input().strip()


def main():
    while True:
        _print_menu()
        try:
            choice = input("Choose an option: ").strip()

            if choice == "1":
                topic = input("What did you learn today? → ").strip()
                add_note(topic)
                print("✅ Note saved!")
            elif choice == "2":
                show_notes()
            elif choice == "3":
                title = input("Enter goal title: ").strip()
                desc = input("Enter goal description (optional): ").strip()
                add_goal(title, desc)
            elif choice == "4":
                list_goals()
            elif choice == "5":
                days = input(
                    "Review notes from how many past days? (default 7): "
                ).strip()
                days = int(days) if days else 7
                sub_prompt = get_sub_prompt_from_console()
                print("🤖 Let me analyze your recent learning...")
                try:
                    summary = generate_study_review_gemini(days, sub_prompt)
                    print("\n🧠 Study Review:\n")
                    print(summary)
                except Exception as e:
                    print(f"⚠️ Oops! Something went wrong: {e}")
            elif choice == "6":
                print("Goodbye, keep shining! 🌟")
                break
            else:
                print("❌ Invalid option. Try again.")
        except KeyboardInterrupt:
            print("\nExiting gracefully. Take care!")
            break
        except Exception as e:
            print(f"⚠️ Oops! Something went wrong: {e}")


if __name__ == "__main__":
    main()
