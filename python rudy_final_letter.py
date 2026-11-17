
import tkinter as tk
from tkinter import ttk

# -----------------------------------------
# RUDY - A LETTER FROM THE HEART
# -----------------------------------------

root = tk.Tk()
root.title("A Letter For Miss Rudyy ❤️")
root.geometry("950x750")
root.minsize(650, 550)

BG_COLORS = [
    "#101827",
    "#21152e",
    "#182333",
    "#101522",
    "#251626"
]

TEXT_COLORS = [
    "#f8e8ed",
    "#ffe4ed",
    "#e5eaff",
    "#f7e5ed",
    "#ffe5ee"
]

ACCENT = "#ff79a8"

current_slide = 0
animation_token = 0

# -----------------------------------------
# SLIDE CONTENT
# -----------------------------------------

slides = [

    {
        "title": "A LITTLE QUESTION FOR YOU 🌷",
        "body": """
Hey, Miss Rudyy!

So, tell me something...

How was your birthday?

Did you enjoy your day?
Did something make you smile?
Did everything go the way you expected?

I genuinely hope your day was beautiful
and filled with little moments of happiness.

And if you want to share your day with me,
I'm here to listen.

Agar dost maanti ho mujhe,
toh sachhe dil se apna din share karna.

And if you don't feel like sharing,
that's completely okay too.

I just hope your birthday was better
than you expected.

You deserved a beautiful day. ❤️
"""
    },

    {
        "title": "WHAT SHOULD I CALL THIS FEELING? 💌",
        "body": """
Honestly, I don't know what this feeling is.

I don't even know what to call it.
Maybe attachment, maybe affection,
or maybe something I should call
ONE-SIDED LOVE.

I'm tired of feeling like I'm the only one
trying to keep this connection alive.

I know you once told me that you
don't feel anything like that
and wanted things to stay casual.

But somehow, I couldn't keep my feelings casual.

I never planned to fall for someone.
I wasn't even looking for love.

And then I found you.

You became the first person
to whom I gave so much of my time,
my tears, my heart and my attention.

I know you might wonder:
How can someone fall for a person
they met through an online platform?

For real, I don't know either.

You made me feel butterflies
when I least expected them.

We have shared almost a year of friendship.
Sometimes you disappeared,
sometimes you came back,
and somehow I kept hoping
that we would stay connected.

I know I became too attached.
I know I feared losing you,
even when I wasn't sure
whether I had a place in your life.

Maybe I was searching for a kind of love
and care that I had missed elsewhere.

And perhaps I expected too much.

But I'm genuinely glad
that I found you in this lifetime.

Thank you for making me feel loved,
even if things didn't mean the same
to both of us.
"""
    },

    {
        "title": "I THINK IT'S TIME TO STEP BACK 🌙",
        "body": """
I think this is where I need to make
a difficult decision.

Maybe this is my last time
writing to you first.

I tried being a friend.
I really tried.

Sometimes I even begged
for the smallest amount of attention.

But I don't want to keep forcing
a connection that should feel natural.

I'm going to try not to text first anymore.

Not because I hate you.
Not because I want revenge.

But because I need to take care
of my own feelings too.

If you ever text me,
I won't pretend you don't exist.
I'll always appreciate hearing from you.

And whatever you decide,
I'll respect it.

I hope my distance brings you peace.
I hope you find your freedom.

Maybe my chapter in your life
ends here.

But please know,
I genuinely wish you the happiest days,
full of laughter, opportunities
and beautiful memories.

Without any burden,
without any expectations,
and without someone like me
making things difficult for you.

I tried, Rudy.
I really did.
"""
    },

    {
        "title": "YOUR ABSENCE HURTS DIFFERENTLY 🥀",
        "body": """
Your absence hurts more
than your presence ever did.

And yes, I'm sorry if I disturbed
your peaceful moments.

I'll survive it.
I'll slowly learn to live
with the silence between us.

But I don't know how long
it will take me to let go.

Maine tumse pehle bhi kaha tha,
aaj bhi kehta hoon...

"Main kisi ko nahi chhodta,
log hi aksar mujhe chhod jaate hain."

Earlier, losing people didn't affect me
this much.

But losing you?
That is going to hurt differently.

Sometimes you talked to me
early in the morning,
sometimes during the day,
sometimes in the evening,
sometimes late at night,
and sometimes until 11.

And you know what?

Maybe you became my 11:11 wish.

A wish I kept making,
even when I knew
it might never come true.

I don't know whether you'll miss me.
I don't know whether you'll notice
my silence.

But I'll always remember
the little conversations,
the random moments
and the happiness you brought.

I hope life treats you gently, Rudy.

And I hope you always have
a reason to smile. ❤️
"""
    },

    {
        "title": "HEY, MISS RUDYY... ❤️",
        "body": """
There is just one last thing
I want you to know.

I don't regret meeting you.

I don't regret the time,
the conversations,
the laughter or even the tears.

You were special to me.

Maybe I'll always carry
a little part of this story
in my heart.

But I also want to learn
to love myself,
to make new memories,
and to find happiness
without depending on one person.

Thank you for everything.

For the butterflies,
for the memories,
for the smiles,
and even for teaching me
how much feelings can hurt.

I hope you find everything
your heart has ever wished for.

Be happy, Miss Rudyy.

Always. 🌷
"""
    }
]

# -----------------------------------------
# MAIN BACKGROUND
# -----------------------------------------

root.configure(bg=BG_COLORS[0])

header = tk.Label(
    root,
    text="A LETTER FROM THE HEART",
    font=("Georgia", 23, "bold"),
    bg=BG_COLORS[0],
    fg=ACCENT,
    pady=22
)
header.pack(fill="x")

subtitle = tk.Label(
    root,
    text="Some feelings are difficult to explain...",
    font=("Georgia", 12, "italic"),
    bg=BG_COLORS[0],
    fg="#d8c5d5"
)
subtitle.pack(pady=(0, 18))

# -----------------------------------------
# SLIDE TITLE
# -----------------------------------------

slide_title = tk.Label(
    root,
    text="",
    font=("Georgia", 19, "bold"),
    wraplength=820,
    bg=BG_COLORS[0],
    fg=ACCENT,
    pady=20
)
slide_title.pack(fill="x")

# -----------------------------------------
# SCROLLABLE MESSAGE AREA
# -----------------------------------------

content_frame = tk.Frame(
    root,
    bg=BG_COLORS[0]
)
content_frame.pack(
    fill="both",
    expand=True,
    padx=45,
    pady=5
)

scrollbar = ttk.Scrollbar(content_frame)
scrollbar.pack(side="right", fill="y")

message_text = tk.Text(
    content_frame,
    wrap="word",
    height=12,
    font=("Georgia", 14),
    bg=BG_COLORS[0],
    fg=TEXT_COLORS[0],
    relief="flat",
    padx=25,
    pady=20,
    spacing1=8,
    spacing3=12,
    cursor="arrow",
    yscrollcommand=scrollbar.set
)

message_text.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.config(command=message_text.yview)

message_text.tag_configure(
    "center",
    justify="center"
)

message_text.tag_configure(
    "final",
    foreground=ACCENT,
    font=("Georgia", 19, "bold"),
    justify="center",
    spacing1=10,
    spacing3=12
)

# -----------------------------------------
# NAVIGATION AREA
# -----------------------------------------

footer = tk.Frame(
    root,
    bg=BG_COLORS[0]
)
footer.pack(
    side="bottom",
    fill="x",
    pady=10
)

previous_button = tk.Button(
    footer,
    text="← Previous",
    font=("Arial", 12, "bold"),
    bg="#454052",
    fg="white",
    activebackground="#66546e",
    relief="flat",
    padx=25,
    pady=12,
    cursor="hand2"
)
previous_button.pack(side="left", padx=40)

next_button = tk.Button(
    footer,
    text="Continue →",
    font=("Arial", 12, "bold"),
    bg=ACCENT,
    fg="#251626",
    activebackground="#ffacc7",
    relief="flat",
    padx=28,
    pady=12,
    cursor="hand2"
)
next_button.pack(side="right", padx=40)

slide_counter = tk.Label(
    footer,
    text="",
    font=("Arial", 11),
    bg=BG_COLORS[0],
    fg="#d9c5d5"
)
slide_counter.pack(side="top", pady=5)

# -----------------------------------------
# FINAL SLIDE ANIMATION
# -----------------------------------------

closing_lines = [
"𝐇𝐞𝐲!",
"𝐌", 
"𝐌𝐢",
"𝐌𝐢𝐬",
"𝐌𝐢𝐬 𝐍",
"𝐌𝐢𝐬 𝐍𝐞",
"𝐌𝐢𝐬 𝐍𝐞𝐡",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝𝐲",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝𝐲𝐲",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝𝐲𝐲 𝐈",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝𝐲𝐲 𝐈 𝐥",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝𝐲𝐲 𝐈 𝐥𝐨",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝𝐲𝐲 𝐈 𝐥𝐨𝐯",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝𝐲𝐲 𝐈 𝐥𝐨𝐯𝐞",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝𝐲𝐲 𝐈 𝐥𝐨𝐯𝐞𝐝",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝𝐲𝐲 𝐈 𝐥𝐨𝐯𝐞𝐝 𝐲",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝𝐲𝐲 𝐈 𝐥𝐨𝐯𝐞𝐝 𝐲𝐨",
"𝐌𝐢𝐬 𝐍𝐞𝐡𝐚 𝐚𝐤𝐚 𝐑𝐮𝐝𝐲𝐲 𝐈 𝐥𝐨𝐯𝐞𝐝 𝐲𝐨𝐮𝐮 😭"
]

def animate_closing(index, token):

    if token != animation_token:
        return

    if current_slide != 4:
        return

    if index < len(closing_lines):

        message_text.config(state="normal")

        message_text.insert(
            "end",
            closing_lines[index] + "\n",
            "final"
        )

        message_text.see("end")
        message_text.config(state="disabled")

        root.after(
            350,
            lambda: animate_closing(index + 1, token)
        )

# -----------------------------------------
# SHOW SLIDES
# -----------------------------------------

def show_slide(index):

    global current_slide, animation_token

    current_slide = index
    animation_token += 1

    token = animation_token

    bg = BG_COLORS[index]
    fg = TEXT_COLORS[index]

    root.configure(bg=bg)

    header.configure(bg=bg)
    subtitle.configure(bg=bg)
    slide_title.configure(bg=bg)
    footer.configure(bg=bg)
    slide_counter.configure(bg=bg)
    content_frame.configure(bg=bg)

    message_text.configure(
        bg=bg,
        fg=fg
    )

    slide_title.configure(
        text=slides[index]["title"],
        fg=ACCENT
    )

    slide_counter.configure(
        text=f"CHAPTER {index + 1} / 5"
    )

    message_text.config(state="normal")
    message_text.delete("1.0", "end")

    message_text.insert(
        "1.0",
        slides[index]["body"].strip()
    )

    message_text.tag_add(
        "center",
        "1.0",
        "end"
    )

    message_text.config(state="disabled")

    message_text.yview_moveto(0)

    if index == 4:

        message_text.config(state="normal")
        message_text.insert("end", "\n\n")
        message_text.config(state="disabled")

        root.after(
            1000,
            lambda: animate_closing(0, token)
        )

    if index == 0:
        previous_button.pack_forget()
    else:
        previous_button.pack(
            side="left",
            padx=40
        )

    if index == 4:
        next_button.config(
            text="Close Letter ✨",
            command=root.destroy
        )
    else:
        next_button.config(
            text="Continue →",
            command=next_slide
        )

# -----------------------------------------
# BUTTON FUNCTIONS
# -----------------------------------------

def next_slide():

    if current_slide < 4:
        show_slide(current_slide + 1)

def previous_slide():

    if current_slide > 0:
        show_slide(current_slide - 1)

previous_button.config(
    command=previous_slide
)

# -----------------------------------------
# START
# -----------------------------------------

show_slide(0)

root.mainloop()
