import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Book App")

        self.recipes = self.load_recipes()  
        self.favorites = self.load_favorites()  

       
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.category_label = tk.Label(self.frame, text="Select Category:")
        self.category_label.grid(row=0, column=0, padx=5)
        self.category_var = tk.StringVar(value="All Categories")
        self.category_menu = tk.OptionMenu(self.frame, self.category_var, "All Categories", "Dessert", "Main Course", "Salad")
        self.category_menu.grid(row=0, column=1, padx=5)

        self.recipe_listbox = tk.Listbox(self.frame, width=40, height=15, bg="lightyellow", fg="black", selectbackground="lightblue")
        self.recipe_listbox.grid(row=1, column=0, columnspan=2, pady=10)
        self.recipe_listbox.bind('<Double-1>', self.show_recipe_details)  # Bind double click to show recipe details

        self.add_button = tk.Button(self.frame, text="Add Recipe", command=self.add_recipe, bg="lightgreen", fg="black")
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        self.edit_button = tk.Button(self.frame, text="Edit Recipe", command=self.edit_recipe, bg="lightcoral", fg="black")
        self.edit_button.grid(row=2, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Recipe", command=self.delete_recipe, bg="red", fg="white")
        self.delete_button.grid(row=3, column=0, padx=5, pady=5)

        self.fav_button = tk.Button(self.frame, text="Add to Favorites", command=self.add_to_favorites, bg="lightpink", fg="black")
        self.fav_button.grid(row=3, column=1, padx=5, pady=5)

        self.show_favs_button = tk.Button(self.frame, text="Show Favorites", command=self.show_favorites, bg="lightblue", fg="black")
        self.show_favs_button.grid(row=4, column=0, padx=5, pady=5)

        self.filter_button = tk.Button(self.frame, text="Filter", command=self.filter_recipes, bg="lightgray", fg="black")
        self.filter_button.grid(row=0, column=2, padx=5)

        self.load_to_listbox() 

    def load_recipes(self):
        try:
            with open('recipes.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_recipes(self):
        with open('recipes.json', 'w') as file:
            json.dump(self.recipes, file)

    def load_favorites(self):
        try:
            with open('favorites.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_favorites(self):
        with open('favorites.json', 'w') as file:
            json.dump(self.favorites, file)

    def add_recipe(self):
        category = simpledialog.askstring("Category", "Enter the category (Dessert, Main Course, Salad, etc.):")
        if not category:
            messagebox.showerror("Error", "Category cannot be empty.")
            return
        
        name = simpledialog.askstring("Recipe Name", "Enter the recipe name:")
        if not name:
            messagebox.showerror("Error", "Recipe name cannot be empty.")
            return
        
        ingredients = simpledialog.askstring("Ingredients", "Enter the ingredients (comma separated):")
        if not ingredients:
            messagebox.showerror("Error", "Ingredients cannot be empty.")
            return

        details = simpledialog.askstring("Recipe Details", "Enter the recipe details:")
        if not details:
            messagebox.showerror("Error", "Recipe details cannot be empty.")
            return

        if category not in self.recipes:
            self.recipes[category] = []

        self.recipes[category].append({"name": name, "ingredients": ingredients, "details": details})
        self.recipe_listbox.insert(tk.END, f"{name} ({category})")
        self.save_recipes()  # Save recipes to file
        messagebox.showinfo("Success", "Recipe added successfully.")

    def edit_recipe(self):
        selected = self.recipe_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a recipe to edit.")
            return

        item_text = self.recipe_listbox.get(selected)
        name = item_text.split(" (")[0]
        category = item_text.split(" (")[1][:-1]

        new_name = simpledialog.askstring("New Recipe Name", "Enter the new recipe name:", initialvalue=name)
        if not new_name:
            messagebox.showerror("Error", "Recipe name cannot be empty.")
            return

        new_ingredients = simpledialog.askstring("New Ingredients", "Enter the new ingredients (comma separated):")
        if not new_ingredients:
            messagebox.showerror("Error", "Ingredients cannot be empty.")
            return

        new_details = simpledialog.askstring("New Recipe Details", "Enter the new recipe details:")
        if not new_details:
            messagebox.showerror("Error", "Recipe details cannot be empty.")
            return

        self.recipes[category] = [recipe for recipe in self.recipes[category] if recipe["name"] != name]
        self.recipes[category].append({"name": new_name, "ingredients": new_ingredients, "details": new_details})

        self.recipe_listbox.delete(selected)
        self.recipe_listbox.insert(selected, f"{new_name} ({category})")
        self.save_recipes()  # Save recipes to file
        messagebox.showinfo("Success", "Recipe edited successfully.")

    def delete_recipe(self):
        selected = self.recipe_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a recipe to delete.")
            return

        item_text = self.recipe_listbox.get(selected)
        name = item_text.split(" (")[0]
        category = item_text.split(" (")[1][:-1]

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the recipe '{name}'?")
        if confirm:
            self.recipes[category] = [recipe for recipe in self.recipes[category] if recipe["name"] != name]
            if not self.recipes[category]:
                del self.recipes[category]

            self.recipe_listbox.delete(selected)
            self.save_recipes()  # Save recipes to file
            messagebox.showinfo("Success", "Recipe deleted successfully.")

    def add_to_favorites(self):
        selected = self.recipe_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a recipe to add to favorites.")
            return

        item_text = self.recipe_listbox.get(selected)
        if item_text in self.favorites:
            messagebox.showwarning("Warning", "This recipe is already in favorites.")
            return

        self.favorites.append(item_text)
        self.save_favorites()  # Save favorites to file
        messagebox.showinfo("Success", "Recipe added to favorites.")

    def show_favorites(self):
        if not self.favorites:
            messagebox.showinfo("Favorites", "No favorite recipes found.")
            return

        fav_text = "\n".join(self.favorites)
        messagebox.showinfo("Favorite Recipes", fav_text)

    def filter_recipes(self):
        category = self.category_var.get()
        self.recipe_listbox.delete(0, tk.END)

        if category == "All Categories":
            for cat, recipes in self.recipes.items():
                for recipe in recipes:
                    self.recipe_listbox.insert(tk.END, f"{recipe['name']} ({cat})")
        else:
            if category in self.recipes:
                for recipe in self.recipes[category]:
                    self.recipe_listbox.insert(tk.END, f"{recipe['name']} ({category})")
            else:
                messagebox.showinfo("Info", f"No recipes found in {category} category.")

    def show_recipe_details(self, event):
        selected = self.recipe_listbox.curselection()
        if not selected:
            return

        item_text = self.recipe_listbox.get(selected)
        name = item_text.split(" (")[0]
        category = item_text.split(" (")[1][:-1]

        for recipe in self.recipes.get(category, []):
            if recipe["name"] == name:
                details = f"Name: {recipe['name']}\nIngredients: {recipe['ingredients']}\nDetails: {recipe['details']}"
                messagebox.showinfo("Recipe Details", details)
                return

    def load_to_listbox(self):
        for cat, recipes in self.recipes.items():
            for recipe in recipes:
                self.recipe_listbox.insert(tk.END, f"{recipe['name']} ({cat})")


root = tk.Tk()
app = RecipeApp(root)
root.mainloop()
