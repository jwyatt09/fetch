import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class LinearRegressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fetch Receipt Predictor")
        self.root.geometry('800x800')
        root.configure(bg='white')

        # Create widgets
        self.label = tk.Label(root, background='white', text="Upload CSV file:")
        self.label.pack(pady=5)

        self.upload_button = tk.Button(root, text="Upload", command=self.upload_csv)
        self.upload_button.pack(pady=5)

        self.run_button = tk.Button(root, text="Make Predictions for 2022", command=self.run_linear_regression)
        self.run_button.pack(pady=5)

        # Create Text widget for displaying results
        self.create_text_widget()

        # Create Figure for the plot
        self.fig, self.ax = plt.subplots(figsize=(5, 3), tight_layout=True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Variables
        self.file_path = None

    def create_text_widget(self):
        self.result_text = tk.Text(self.root, background='white', height=15, width=35)
        self.result_text.pack(pady=5)

    def upload_csv(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            print(f"File uploaded: {self.file_path}")

    def run_linear_regression(self):
        if not self.file_path:
            print("Please upload a CSV file first.")
            return

    
        df = pd.read_csv(self.file_path)

        daily_receipts = np.array([df['Receipt_Count']], dtype=np.float32)

        # Feature scaling
        receipts_mean = daily_receipts.mean()
        receipts_std = daily_receipts.std()

        daily_receipts = (daily_receipts - receipts_mean) / receipts_std

        # Day indices and scaling
        days = np.arange(1, 366, dtype=np.float32)

        days_mean = days.mean()
        days_std = days.std()

        days = (days - days_mean) / days_std

        # Model parameters
        learning_rate = 0.01
        epochs = 1000

        # Model variables
        W_day = tf.Variable(np.random.randn(), name="weight_day")
        b = tf.Variable(np.random.randn(), name="bias")

        # Model
        def linear_regression(day):
            return tf.add(tf.multiply(day, W_day), b)

        # Loss function (mean squared error)
        def mean_squared_error(y_pred, y_true):
            return tf.reduce_mean(tf.square(y_pred - y_true))

        # Optimizer
        optimizer = tf.keras.optimizers.legacy.SGD(learning_rate)

        # Training
        for epoch in range(epochs):
            with tf.GradientTape() as tape:
                predictions = linear_regression(days)
                loss = mean_squared_error(predictions, daily_receipts)

            gradients = tape.gradient(loss, [W_day, b])
            optimizer.apply_gradients(zip(gradients, [W_day, b]))

        # Make predictions
        predictions = linear_regression(days)

        # Denormalize predictions
        predictions = predictions * receipts_std + receipts_mean

        # Create a DataFrame with the dates for 2022 as the index
        date_index = pd.date_range(start='2022-01-01', end='2022-12-31')
        predictions_2022 = pd.DataFrame(data={'Predicted_Receipts': predictions}, index=date_index)

        # get monthly totals
        monthly_totals = predictions_2022.resample('M').sum()

        # Clear any previous text in the Text widget
        self.result_text.delete(1.0, tk.END)

        # Display monthly_totals in the Text widget
        self.result_text.insert(tk.END, monthly_totals)

        # Plot monthly_totals
        self.ax.clear()
        monthly_totals.plot(kind='bar', ax=self.ax)

        # Customize axes formatting
        self.ax.get_yaxis().get_major_formatter().set_scientific(False)
        self.ax.get_yaxis().get_major_formatter().set_useOffset(False)

        # Customize x-axis labels
        self.ax.set_xticklabels(monthly_totals.index.strftime('%B'), rotation=45, ha='right')

        self.ax.set_title('Monthly Receipt Totals for 2022')
        self.ax.set_xlabel('Month')
        self.ax.set_ylabel('Total Receipts')

        self.ax.legend().set_visible(False)

        # Update the plot
        self.canvas.draw()

        print("Linear regression completed. Results displayed.")

        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = LinearRegressionApp(root)
    root.mainloop()
