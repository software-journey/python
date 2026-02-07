“””
Like LEGO? Love Python! - Episode 1
Additional Examples & Experiments

More brick-building adventures! These examples expand on the basic LegoBrick
class with additional demonstrations, edge cases, and experiments.

Think of this as the “advanced techniques” section of the instruction manual -
the part where they show you can build a spaceship AND a pirate ship from
the same pieces.

Read the full article: https://dev.to/the-software-s-journey/like-lego-love-python-2104
“””

from lego_brick import LegoBrick

# =============================================================================

# Example 1: Building a Brick Collection

# =============================================================================

def example_brick_collection():
“”“Create a collection of various bricks and analyze them.”””
print(”=” * 60)
print(“Example 1: Building a Brick Collection”)
print(”=” * 60 + “\n”)

```
# Create a variety pack of bricks
brick_collection = [
    LegoBrick("red", 2, 4),
    LegoBrick("blue", 2, 2),
    LegoBrick("green", 1, 8),
    LegoBrick("yellow", 4, 2),
    LegoBrick("black", 1, 1),  # The infamous 1x1 - destroyer of vacuums
]

print(f"📦 Our collection has {len(brick_collection)} bricks:\n")

for i, brick in enumerate(brick_collection, 1):
    print(f"  {i}. {brick.describe()}")

# Calculate total studs (because why not?)
total_studs = sum(brick.studs for brick in brick_collection)
print(f"\n🔢 Total studs across all bricks: {total_studs}")
print(f"   (That's a lot of potential pain for bare feet!)\n")
```

# =============================================================================

# Example 2: Finding Compatible Bricks

# =============================================================================

def example_compatible_bricks():
“”“Demonstrate finding which bricks can connect to each other.”””
print(”=” * 60)
print(“Example 2: Finding Compatible Bricks”)
print(”=” * 60 + “\n”)

```
target_brick = LegoBrick("red", 2, 4)
test_bricks = [
    LegoBrick("blue", 4, 2),    # Should connect
    LegoBrick("green", 2, 2),   # Should connect
    LegoBrick("yellow", 1, 8),  # Should NOT connect
    LegoBrick("black", 4, 4),   # Should connect
]

print(f"🎯 Testing connections for: {target_brick.describe()}\n")

compatible_bricks = []
incompatible_bricks = []

for brick in test_bricks:
    if target_brick.can_connect_to(brick):
        compatible_bricks.append(brick)
        print(f"  ✅ CAN connect to: {brick.describe()}")
    else:
        incompatible_bricks.append(brick)
        print(f"  ❌ CANNOT connect to: {brick.describe()}")

print(f"\n📊 Results:")
print(f"  Compatible: {len(compatible_bricks)}")
print(f"  Incompatible: {len(incompatible_bricks)}\n")
```

# =============================================================================

# Example 3: The Brick Counter (Using Class Attributes)

# =============================================================================

class CountedLegoBrick(LegoBrick):
“””
An enhanced LEGO brick that counts how many bricks have been created.

```
This demonstrates a more advanced concept: class attributes (shared across
all instances) vs. instance attributes (unique to each brick).

Think of it as the factory keeping track of production numbers.
"""

# Class attribute - shared across ALL bricks of this type
total_bricks_created = 0

def __init__(self, color, length, width):
    """Initialize a counted brick and increment the counter."""
    super().__init__(color, length, width)  # Call parent class __init__
    CountedLegoBrick.total_bricks_created += 1
    self.brick_number = CountedLegoBrick.total_bricks_created

def describe(self):
    """Return description including the brick's production number."""
    base_description = super().describe()
    return f"{base_description} (Brick #{self.brick_number})"
```

def example_brick_counter():
“”“Demonstrate tracking brick creation with class attributes.”””
print(”=” * 60)
print(“Example 3: The Brick Counter”)
print(”=” * 60 + “\n”)

```
print("🏭 Starting production...\n")

# Create several counted bricks
bricks = [
    CountedLegoBrick("red", 2, 4),
    CountedLegoBrick("blue", 2, 2),
    CountedLegoBrick("green", 1, 8),
    CountedLegoBrick("yellow", 4, 2),
]

print("📦 Production Results:\n")
for brick in bricks:
    print(f"  • {brick.describe()}")

print(f"\n📊 Total bricks manufactured: {CountedLegoBrick.total_bricks_created}")
print(f"   (The factory is running smoothly!)\n")
```

# =============================================================================

# Example 4: Brick Color Analysis

# =============================================================================

def example_color_analysis():
“”“Analyze brick colors in a collection.”””
print(”=” * 60)
print(“Example 4: Brick Color Analysis”)
print(”=” * 60 + “\n”)

```
# Create a mixed bag of bricks
bricks = [
    LegoBrick("red", 2, 4),
    LegoBrick("red", 2, 2),
    LegoBrick("blue", 4, 2),
    LegoBrick("blue", 2, 4),
    LegoBrick("blue", 1, 1),
    LegoBrick("green", 2, 2),
    LegoBrick("yellow", 2, 4),
]

# Count bricks by color
color_counts = {}
for brick in bricks:
    color_counts[brick.color] = color_counts.get(brick.color, 0) + 1

print("🎨 Color Distribution:\n")
for color, count in sorted(color_counts.items()):
    bar = "█" * count
    print(f"  {color.capitalize():8} {bar} ({count})")

# Find most common color
most_common_color = max(color_counts, key=color_counts.get)
print(f"\n🏆 Most common color: {most_common_color.capitalize()}")
print(f"   (Clearly someone has a favorite!)\n")
```

# =============================================================================

# Example 5: The Experimental Brick Lab

# =============================================================================

def example_experimental_bricks():
“”“Create some unusual bricks to test edge cases.”””
print(”=” * 60)
print(“Example 5: The Experimental Brick Lab”)
print(”=” * 60 + “\n”)

```
print("🧪 Testing unusual brick configurations:\n")

# The minimum viable brick
tiny_brick = LegoBrick("transparent", 1, 1)
print(f"  Tiny: {tiny_brick.describe()}")

# The long boi
long_brick = LegoBrick("gray", 1, 16)
print(f"  Long: {long_brick.describe()}")

# The chunky brick
chunky_brick = LegoBrick("brown", 8, 8)
print(f"  Chunky: {chunky_brick.describe()}")

# The imaginary brick (what if LEGO made weird colors?)
weird_brick = LegoBrick("neon-octarine", 3, 7)
print(f"  Weird: {weird_brick.describe()}")

print("\n✨ All experimental bricks created successfully!")
print("   (LEGO lawyers have not yet sent cease and desist letters)\n")
```

# =============================================================================

# RUN ALL EXAMPLES

# =============================================================================

if **name** == “**main**”:
print(”\n🧱 LEGO BRICK EXAMPLES & EXPERIMENTS 🧱\n”)
print(“Running all example demonstrations…\n”)

```
example_brick_collection()
print()

example_compatible_bricks()
print()

example_brick_counter()
print()

example_color_analysis()
print()

example_experimental_bricks()

print("=" * 60)
print("✅ All examples completed successfully!")
print("=" * 60)
print("\nNow go forth and build amazing things! 🚀")
print("(Just remember: with great power comes great responsibility...)")
print("(And also a lot of tiny plastic pieces to organize.)\n")
```
