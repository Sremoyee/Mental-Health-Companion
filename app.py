import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Define the classes for each screen. The UI is defined in the .kv file.
class WelcomeScreen(Screen):
    pass

class CheckinScreen(Screen):
    pass

class ReportScreen(Screen):
    pass

# Main App Class
class WellnessApp(App):
    def build(self):
        # Kivy will automatically load the 'wellness.kv' file as the root widget.
        pass

    def generate_personalized_tips(self, mood, stress, sleep, energy, social):
        """Generates tips by analyzing each metric individually."""
        tips = []
        positives = []

        # Analyze mood
        if mood < 4:
            tips.append(
                "[b]For Your Mood:[/b]\n"
                "- Connect with a friend or loved one today.\n"
                "- Spend 15 minutes on a hobby you enjoy."
            )
        elif mood > 7:
            positives.append("It's wonderful that your mood is positive!")

        # Analyze stress (Note: high stress value is bad)
        if stress > 6:
            tips.append(
                "[b]To Manage Stress:[/b]\n"
                "- Try a 5-minute guided meditation or deep breathing exercise.\n"
                "- Take a short walk to clear your head."
            )
        elif stress < 3:
            positives.append("You're managing stress very well.")

        # Analyze sleep
        if sleep < 4:
            tips.append(
                "[b]To Improve Sleep:[/b]\n"
                "- Avoid screens (phone, TV) for an hour before bed.\n"
                "- Create a relaxing bedtime routine, like reading a book."
            )
        elif sleep > 7:
            positives.append("Great job on getting quality sleep!")

        # Analyze Energy Level
        if energy < 4:
            tips.append(
                "[b]To Boost Energy:[/b]\n"
                "- Ensure you are staying hydrated by drinking water.\n"
                "- A short, brisk walk can significantly increase energy."
            )
        elif energy > 7:
            positives.append("You have a high energy level, which is fantastic!")

        # Analyze Social Connection
        if social < 4:
            tips.append(
                "[b]For Social Connection:[/b]\n"
                "- Reach out to one friend today, even with a simple text.\n"
                "- Consider joining a local group or club with shared interests."
            )
        elif social > 7:
            positives.append("Feeling socially connected is a key part of wellness.")


        # Combine all feedback into a final message
        if not tips and not positives:
             return "You're in a balanced state. Keep up the great work with your self-care routines!"
        
        recommendation = ""
        if positives:
            recommendation += "[b]What's Going Well:[/b]\n" + "\n".join(positives) + "\n\n"
        
        if tips:
            recommendation += "[b]Personalized Suggestions:[/b]\n" + "\n\n".join(tips)
        
        return recommendation.strip()

    def calculate_wellness(self):
        """Calculates score, updates the report screen, and switches to it."""
        checkin_screen = self.root.get_screen('checkin')
        
        mood = int(checkin_screen.ids.mood_slider.value)
        stress = int(checkin_screen.ids.stress_slider.value)
        sleep = int(checkin_screen.ids.sleep_slider.value)
        energy = int(checkin_screen.ids.energy_slider.value)
        social = int(checkin_screen.ids.social_slider.value)

        # Updated wellness score formula
        score = (mood + (10 - stress) + sleep + energy + social) / 5

        recommendation = self.generate_personalized_tips(mood, stress, sleep, energy, social)

        result_text = (
            f"[b]Your Wellness Snapshot:[/b]\n\n"
            f"  - Mood: {mood}/10\n"
            f"  - Stress Level: {stress}/10\n"
            f"  - Sleep Quality: {sleep}/10\n"
            f"  - Energy Level: {energy}/10\n"
            f"  - Social Connection: {social}/10\n\n"
            f"[b]Overall Score: {score:.1f}/10[/b]\n\n"
            f"{recommendation}"
        )
        
        report_screen = self.root.get_screen('report')
        report_screen.ids.result_label.text = result_text

        self.root.current = 'report'
    
    def reset_app(self):
        """Resets sliders and returns to the welcome screen."""
        checkin_screen = self.root.get_screen('checkin')
        checkin_screen.ids.mood_slider.value = 5
        checkin_screen.ids.stress_slider.value = 5
        checkin_screen.ids.sleep_slider.value = 5
        checkin_screen.ids.energy_slider.value = 5
        checkin_screen.ids.social_slider.value = 5
        
        self.root.current = 'welcome'

if __name__ == '__main__':
    WellnessApp().run()