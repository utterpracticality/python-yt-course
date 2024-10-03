from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "Get busy living or get busy dying. – Stephen King",
    "You only live once, but if you do it right, once is enough. – Mae West",
    "The purpose of our lives is to be happy. – Dalai Lama",
    "Life is really simple, but we insist on making it complicated. – Confucius",
    "May you live all the days of your life. – Jonathan Swift",
    "Life itself is the most wonderful fairy tale. – Hans Christian Andersen",
    "Do not take life too seriously. You will never get out of it alive. – Elbert Hubbard",
    "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
    "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
    "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Everything you’ve ever wanted is on the other side of fear. – George Addair",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "Believe you can and you’re halfway there. – Theodore Roosevelt",
    "The only way to achieve the impossible is to believe it is possible. – Charles Kingsleigh",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It is never too late to be what you might have been. – George Eliot",
    "You don’t have to be great to start, but you have to start to be great. – Zig Ziglar",
    "I find that the harder I work, the more luck I seem to have. – Thomas Jefferson",
    "Success is walking from failure to failure with no loss of enthusiasm. – Winston Churchill",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "If you can dream it, you can achieve it. – Zig Ziglar",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "The secret of getting ahead is getting started. – Mark Twain",
    "Start where you are. Use what you have. Do what you can. – Arthur Ashe",
    "What we think, we become. – Buddha",
    "Perfection is not attainable, but if we chase perfection we can catch excellence. – Vince Lombardi",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "The best way to predict the future is to create it. – Peter Drucker",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "I can’t change the direction of the wind, but I can adjust my sails to always reach my destination. – Jimmy Dean",
    "The biggest adventure you can take is to live the life of your dreams. – Oprah Winfrey",
    "The only place where success comes before work is in the dictionary. – Vidal Sassoon",
    "Don’t be afraid to give up the good to go for the great. – John D. Rockefeller",
    "Challenges are what make life interesting and overcoming them is what makes life meaningful. – Joshua J. Marine",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "If you’re going through hell, keep going. – Winston Churchill",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "The best way out is always through. – Robert Frost",
    "Act as if what you do makes a difference. It does. – William James",
    "The only person you are destined to become is the person you decide to be. – Ralph Waldo Emerson",
    "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
    "With the new day comes new strength and new thoughts. – Eleanor Roosevelt",
    "The best revenge is massive success. – Frank Sinatra",
    "The road to success and the road to failure are almost exactly the same. – Colin R. Davis"
]

@app.route("/")
def index():
    quote = random.choice(quotes)
    return render_template("index.html", daily_quote=quote, all_quotes=quotes)

if __name__ == "__main__":
    app.run()