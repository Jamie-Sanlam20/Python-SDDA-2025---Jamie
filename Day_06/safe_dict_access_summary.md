# Safe Dictionary Access in Python

## Case 1: Direct Access with Square Brackets - KeyError Risk

When accessing a dictionary key that doesn't exist using square brackets, Python raises a `KeyError`:

```python
spiderman = {
    "name": "Peter Parker",
    "age": 18,
    "team_name": "Avengers",
    "team": ["Iron Man", "Thor", "Hulk", "Captain America"]
}

print(spiderman['height'])  # KeyError: 'height'
```

## Case 2: Successful Direct Access

When the key exists, direct access works fine:

```python
captain_america = {
    "name": "Steve Rogers 🦸‍♂️",
    "age": 100,
    "height": 185
}

print(captain_america["height"])  # Output: 185
```

## Case 3: Safe Access with `.get()` Method

Using the `.get()` method to safely access a key that exists:

```python
spiderman = {
    "name": "Peter Parker",
    "age": 18,
    "team_name": "Avengers",
    "team": ["Iron Man", "Thor", "Hulk", "Captain America"]
}

spiderman.get('age')  # Returns: 18
```

## Case 4: Safe Access with `.get()` for Non-existent Keys

The `.get()` method returns `None` for non-existent keys instead of raising an error:

```python
print(spiderman.get('height'))  # Output: None ✅ - Safe access
print(spiderman['height'])      # KeyError ❌ - Unsafe access
```

## Case 5: Nested Dictionary Access

Accessing nested dictionaries can be tricky:

```python
captain_america = {
    "name": "Steve Rogers 🦸‍♂️",
    "age": 100,
    "height": 185,
    "address": {
        "city": "Brooklyn",
        "country": "US"
    }
}

spiderman = {
    "name": "Peter Parker",
    "age": 18,
    "team_name": "Avengers",
    "team": ["Iron Man", "Thor", "Hulk", "Captain America"],
    "address": {}
}

# Direct access to nested keys
captain_america['address']['city']  # Returns: 'Brooklyn'

# This would raise a KeyError:
# spiderman['address']['city']

# Safe access to nested keys
print(spiderman.get('address').get("city"))  # Output: None
```

## Case 6: Safe Access with Default Values

The `.get()` method can provide default values for non-existent keys:

```python
spiderman = {
    "name": "Peter Parker",
    "age": 18,
    "team_name": "Avengers",
    "team": ["Iron Man", "Thor", "Hulk", "Captain America"],
    "address": {}
}

spiderman.get('height', 175)  # Returns: 175 (default value)
```

## Case 7: Default Values with Existing Keys

When the key exists, `.get()` returns the actual value, not the default:

```python
spiderman = {
    "name": "Peter Parker",
    "age": 18,
    "team_name": "Avengers",
    "team": ["Iron Man", "Thor", "Hulk", "Captain America"],
    "height": 185,
    "address": {}
}

spiderman.get('height', 175)  # Returns: 185 (actual value, not default)
```

## Summary

1. **Square Bracket Access (`dict['key']`)**:

   - Fast and direct
   - Raises `KeyError` if key doesn't exist
   - Use when you're certain the key exists

2. **`.get()` Method (`dict.get('key')`)**:

   - Safe access that returns `None` if key doesn't exist
   - Can specify a default value: `dict.get('key', default_value)`
   - Ideal for cases where keys might be missing

3. **Nested Dictionary Access**:
   - Chain `.get()` calls for safe nested access: `dict.get('outer_key').get('inner_key')`
   - Prevents KeyError in nested structures
