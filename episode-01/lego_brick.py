“””
Like LEGO? Love Python! - Episode 1
Building Your First Brick (Defining Classes)

This module contains the LegoBrick class - your first blueprint for creating
virtual LEGO bricks in Python. Because who needs the real thing when you can
have infinitely stackable digital bricks that never hurt your feet?

Read the full article: https://dev.to/the-software-s-journey/like-lego-love-python-2104
“””

class LegoBrick:
“””
A virtual LEGO brick with color, dimensions, and the ability to describe itself.

```
Think of this as the master mold at LEGO headquarters - one blueprint that can
create thousands of identical (but individually configured) bricks.

Attributes:
    color (str): The color of the brick (e.g., "red", "blue", "that-weird-green-nobody-uses")
    length (int): Length of the brick in LEGO units
    width (int): Width of the brick in LEGO units
    studs (int): Number of studs on top (auto-calculated because we're fancy)
"""

def __init__(self, color, length, width):
    """
    Initialize a new LEGO brick.
    
    This is the magic factory method that runs automatically when you create
    a new brick. It's like the injection molding process, but with less melted plastic.
    
    Args:
        color (str): What color is this brick? Be creative! "red", "blue", "existential-crisis-gray"
        length (int): How many units long? (e.g., 2 for a 2x4 brick)
        width (int): How many units wide? (e.g., 4 for a 2x4 brick)
    
    Example:
        >>> my_brick = LegoBrick("red", 2, 4)
        >>> print(my_brick.color)
        'red'
    """
    self.color = color
    self.length = length
    self.width = width
    self.studs = length * width  # Auto-calculate studs because we're lazy (efficiently lazy)

def describe(self):
    """
    Return a human-readable description of this brick.
    
    Because bricks deserve to introduce themselves properly.
    
    Returns:
        str: A friendly description of the brick's attributes
    
    Example:
        >>> brick = LegoBrick("blue", 2, 2)
        >>> print(brick.describe())
        'A blue 2x2 brick with 4 studs'
    """
    return f"A {self.color} {self.length}x{self.width} brick with {self.studs} studs"

def can_connect_to(self, other_brick):
    """
    Check if this brick can connect to another brick.
    
    In real LEGO, this involves complex engineering. In our simplified version,
    we just check if the dimensions are compatible (length matches width or vice versa).
    
    Note: This is a VERY simplified connection logic. Real LEGO physics are way more
    complicated, involving quantum mechanics, dark matter, and Danish wizardry.
    
    Args:
        other_brick (LegoBrick): The brick we're trying to connect to
    
    Returns:
        bool: True if bricks can connect, False if they're incompatible (like my ex)
    
    Example:
        >>> brick1 = LegoBrick("red", 2, 4)
        >>> brick2 = LegoBrick("blue", 4, 2)
        >>> print(brick1.can_connect_to(brick2))
        True
    """
    # Simplified logic: bricks can connect if dimensions match
    return (self.length == other_brick.width or 
            self.width == other_brick.length)
```

# =============================================================================

# DEMO: Let’s build some bricks!

# =============================================================================

if **name** == “**main**”:
print(“🧱 Welcome to the LEGO Brick Factory! 🧱\n”)

```
# Create some bricks (stamping them from our blueprint)
print("Manufacturing some bricks...\n")

red_brick = LegoBrick("red", 2, 4)
blue_brick = LegoBrick("blue", 4, 2)
green_brick = LegoBrick("green", 1, 8)  # That weird piece nobody ever uses
yellow_brick = LegoBrick("yellow", 2, 2)

# Describe our bricks
print("📦 Brick Inventory:")
print(f"  • {red_brick.describe()}")
print(f"  • {blue_brick.describe()}")
print(f"  • {green_brick.describe()}")
print(f"  • {yellow_brick.describe()}\n")

# Test connectivity (the moment of truth!)
print("🔗 Connection Tests:")
print(f"  Can red (2x4) connect to blue (4x2)? {red_brick.can_connect_to(blue_brick)}")
print(f"  Can red (2x4) connect to yellow (2x2)? {red_brick.can_connect_to(yellow_brick)}")
print(f"  Can green (1x8) connect to yellow (2x2)? {green_brick.can_connect_to(yellow_brick)}\n")

# Access individual attributes (because we can!)
print("🎨 Brick Details:")
print(f"  The red brick is {red_brick.color} and has {red_brick.studs} studs")
print(f"  The blue brick is {blue_brick.length} units long")
print(f"  The green brick has {green_brick.width} units of width\n")

print("✨ Success! You've mastered the art of digital LEGO brick creation!")
print("   (Now if only organizing real LEGO was this easy...)\n")
```
