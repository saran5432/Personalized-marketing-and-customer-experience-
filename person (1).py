import tkinter as tk
from tkinter import messagebox
import random

# ========== MARKETING AI ENGINE ==========

class MarketingAI:
    def _init_(self):
        self.products_by_interest = {
            "fitness": ["Smart Gym Mirror", "Adjustable Dumbbells", "Fitness Tracker Watch"],
            "technology": ["AI Voice Assistant", "Wireless Charging Pad", "Smart Thermostat"],
            "fashion": ["Virtual Stylist Subscription", "Smart Jewelry", "Trend Alert Box"],
            "food": ["Healthy Snack Box", "Smart Air Fryer", "Recipe App"],
            "travel": ["Smart Luggage", "Universal Adapter", "Portable Wi-Fi Hotspot"]
        }

        self.products_by_age = {
            "teen": ["Gaming Headset", "Bluetooth Speaker", "Portable Power Bank"],
            "young_adult": ["Smartwatch", "Ergonomic Laptop Stand", "Subscription Box"],
            "adult": ["Noise-Cancelling Headphones", "Smart Home Hub", "Online Course Pass"],
            "senior": ["Digital Photo Frame", "Health Monitor Watch", "E-Reader"]
        }

    def recommend(self, interests, age):
        interests = interests.lower()
        interest_matches = []

        for key in self.products_by_interest:
            if key in interests:
                interest_matches.extend(self.products_by_interest[key])

        # Age-based category
        if age < 18:
            age_group = "teen"
        elif 18 <= age < 30:
            age_group = "young_adult"
        elif 30 <= age < 60:
            age_group = "adult"
        else:
            age_group = "senior"

        age_products = self.products_by_age.get(age_group, [])

        all_recommendations = list(set(interest_matches + age_products))

        if not all_recommendations:
            # fallback to random
            all_recommendations = [item for sublist in self.products_by_interest.values() for item in sublist]

        return random.sample(all_recommendations, min(3, len(all_recommendations)))


# ========== GUI APPLICATION ==========

class MarketingApp:
    def _init_(self, root):
        self.root = root
        self.root.title("AI Personalized Marketing App")
        self.root.geometry("550x500")
        self.root.configure(bg="#eaf6fb")

        self.ai = MarketingAI()
        self.build_gui()

    def build_gui(self):
        tk.Label(self.root, text="Smart Marketing Assistant", font=("Helvetica", 20, "bold"), fg="#007acc", bg="#eaf6fb").pack(pady=20)

        # Name input
        tk.Label(self.root, text="Enter your name:", font=("Helvetica", 12), bg="#eaf6fb").pack()
        self.name_entry = tk.Entry(self.root, font=("Helvetica", 12), width=40)
        self.name_entry.pack(pady=5)

        # Age input
        tk.Label(self.root, text="Enter your age:", font=("Helvetica", 12), bg="#eaf6fb").pack()
        self.age_entry = tk.Entry(self.root, font=("Helvetica", 12), width=40)
        self.age_entry.pack(pady=5)

        # Interest input
        tk.Label(self.root, text="Enter your interests (e.g., fitness, fashion, travel):", font=("Helvetica", 12), bg="#eaf6fb").pack()
        self.interest_entry = tk.Entry(self.root, font=("Helvetica", 12), width=40)
        self.interest_entry.pack(pady=5)

        # Button
        tk.Button(self.root, text="Get Personalized Recommendations", font=("Helvetica", 12, "bold"),
                  bg="#28a745", fg="white", command=self.generate_recommendations).pack(pady=20)

        self.output_label = tk.Label(self.root, text="", font=("Helvetica", 12), wraplength=500, justify="left", bg="#eaf6fb")
        self.output_label.pack(pady=10)

    def generate_recommendations(self):
        name = self.name_entry.get().strip()
        age_text = self.age_entry.get().strip()
        interests = self.interest_entry.get().strip()

        # Validation
        if not name or not age_text or not interests:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            age = int(age_text)
        except ValueError:
            messagebox.showerror("Invalid Age", "Please enter a valid number for age.")
            return

        recommendations = self.ai.recommend(interests, age)
        formatted = f"Hi {name}, here are your personalized recommendations:\n\n"
        formatted += "\n".join(f"✔ {item}" for item in recommendations)
        self.output_label.config(text=formatted)


# ========== RUN APP ==========

if _name_ == '_main_':
    root = tk.Tk()
    app = MarketingApp(root)
    root.mainloop()