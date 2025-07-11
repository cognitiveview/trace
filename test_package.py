"""
Quick test script for rai-trace package
"""

def test_imports():
    """Test that imports work correctly"""
    try:
        # Test package import
        import rai_trace
        print(f"✅ Package imported successfully")
        print(f"Version: {rai_trace.__version__}")
        
        # Test submodule import
        from rai_trace.plugins.sample import hello_world, add_numbers
        print("✅ Submodule imports work")
        
        # Test functions
        greeting = hello_world("Developer")
        print(f"✅ hello_world(): {greeting}")
        
        result = add_numbers(10, 5)
        print(f"✅ add_numbers(10, 5): {result}")
        
        print("\n🎉 All tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_imports()