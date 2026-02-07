# Episode 1: Building Your First Brick 🧱

**[📖 Read the full article on Dev.to](https://dev.to/the-software-s-journey/like-lego-love-python-2104)**

Welcome to Episode 1, where we learn that Python classes are just LEGO instruction manuals you write yourself! This episode covers the fundamentals of defining classes in Python using everyone’s favorite building blocks as a teaching aid.

## 🎯 What You’ll Learn

- **Class Definition**: How to create blueprints (classes) for objects
- **The `__init__()` Method**: Your brick factory’s assembly line
- **Instance Attributes**: What each brick knows about itself (`self.color`, `self.studs`, etc.)
- **Instance Methods**: What your bricks can do (`describe()`, `can_connect_to()`)
- **Creating Instances**: Actually manufacturing bricks from your blueprint

## 📁 Files in This Episode

### `lego_brick.py`

The main event! Contains the `LegoBrick` class definition with:

- Color, length, and width attributes
- Auto-calculated studs (because we’re efficient like that)
- A `describe()` method for brick self-awareness
- A `can_connect_to()` method for checking compatibility
- Demo code showing everything in action

**Run it:**

```bash
python lego_brick.py
```

**Expected Output:**

```
🧱 Welcome to the LEGO Brick Factory! 🧱

Manufacturing some bricks...

📦 Brick Inventory:
  • A red 2x4 brick with 8 studs
  • A blue 4x2 brick with 8 studs
  • A green 1x8 brick with 8 studs
  • A yellow 2x2 brick with 4 studs

🔗 Connection Tests:
  Can red (2x4) connect to blue (4x2)? True
  Can red (2x4) connect to yellow (2x2)? True
  Can green (1x8) connect to yellow (2x2)? False

[... and more ...]
```

### `examples.py`

Extended examples and experiments including:

- **Brick Collections**: Managing multiple bricks in lists
- **Compatibility Testing**: Finding which bricks work together
- **Brick Counter**: Advanced example using class attributes
- **Color Analysis**: Statistical analysis of your brick collection
- **Experimental Bricks**: Testing edge cases and weird configurations

**Run it:**

```bash
python examples.py
```

This will run all 5 example demonstrations automatically, showing various ways to use and extend the `LegoBrick` class.

## 🚀 Quick Start

1. **Read the article first**: [Like LEGO? Love Python! - Episode 1](https://dev.to/the-software-s-journey/like-lego-love-python-2104)
1. **Run the main demo**: `python lego_brick.py`
1. **Explore examples**: `python examples.py`
1. **Experiment**: Modify the code, create your own brick types!

## 🎓 Key Concepts Explained

### Classes as Blueprints

```python
class LegoBrick:
    """The master blueprint for all LEGO bricks"""
    pass
```

Just like LEGO designs the mold before manufacturing bricks, you define the class before creating instances.

### The `__init__()` Constructor

```python
def __init__(self, color, length, width):
    self.color = color
    self.length = length
    self.width = width
    self.studs = length * width
```

This runs automatically when you create a brick. It’s the injection molding process for your digital bricks!

### The Mysterious `self`

```python
my_brick = LegoBrick("red", 2, 4)
# Python automatically passes my_brick as 'self' to __init__()
```

`self` is the brick talking about itself. When you call `my_brick.describe()`, the brick knows “I am red, I am 2x4, I have 8 studs.”

### Instance Methods

```python
def describe(self):
    return f"A {self.color} {self.length}x{self.width} brick"
```

Methods are behaviors your bricks can perform. They’re like having tiny instruction booklets attached to each brick.

## 🧪 Try These Experiments

1. **Create a new brick type**:
   
   ```python
   class SpecialBrick(LegoBrick):
       def __init__(self, color, length, width, special_feature):
           super().__init__(color, length, width)
           self.special_feature = special_feature
   ```
1. **Add a new method**:
   
   ```python
   def calculate_area(self):
       return self.length * self.width
   ```
1. **Build a brick tower**:
   
   ```python
   class BrickTower:
       def __init__(self):
           self.bricks = []
       
       def add_brick(self, brick):
           self.bricks.append(brick)
   ```

## 📊 Code Statistics

- **Lines of Code**: ~150 (main class + demo)
- **Methods**: 3 (including `__init__()`)
- **Attributes**: 4 per brick
- **Puns**: Too many to count
- **Feet Saved**: Infinite (they’re digital bricks!)

## 🤔 Common Questions

**Q: Why is `self` always the first parameter?**  
A: It’s Python convention. `self` refers to the specific instance calling the method. Python passes it automatically.

**Q: Can I name it something other than `self`?**  
A: Technically yes, but don’t. The Python community will judge you silently. Use `self`.

**Q: Do I have to use `__init__()`?**  
A: No! But it’s the standard way to initialize instance attributes. Without it, your class is like a LEGO brick mold without any instructions.

**Q: Why calculate studs automatically?**  
A: Because we’re programmers and we’re lazy (in the good way). Why make users calculate something we can derive from existing data?

## 🎯 Next Steps

Ready for more? Check out **Episode 2: Inheritance** where we learn how to create specialized bricks that inherit from parent classes.

Spoiler: `class SpecializedBrick(LegoBrick)` is like LEGO Technic - still LEGO, but with gears, motors, and existential questions about identity.

## 🐛 Found a Bug?

If you spot an issue with the code or have suggestions:

1. Check if it’s mentioned in the article
1. Open an issue on the [main repository](https://github.com/software-journey/python)
1. Submit a pull request with a fix (bonus points for LEGO-themed commit messages)

## 📚 Additional Resources

- **Article**: [Dev.to - Like LEGO? Love Python! Episode 1](https://dev.to/the-software-s-journey/like-lego-love-python-2104)
- **Main Repository**: [software-journey/python](https://github.com/software-journey/python)
- **Python Docs**: [Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- **LEGO Brick Dimensions**: [For the truly obsessed](https://bricks.stackexchange.com/questions/288/what-are-the-dimensions-of-a-lego-brick)

-----

**Happy Building! 🎉**

*Remember: In LEGO, the only limit is your imagination (and the number of bricks you have).*  
*In Python, the only limit is your imagination (and possibly memory, but let’s not worry about that yet).*

-----

*Built with ❤️ and an unreasonable number of LEGO puns*
