"""
Verify Setup Script
Run this script to check that your environment is correctly configured.
Usage: python src/verify_setup.py
"""

import sys
import os


def check_python_version():
    """Check Python version is 3.10 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print(f"❌ Python 3.10+ required. You have {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_dependencies():
    """Check required packages are installed."""
    required = [
        ("dotenv", "python-dotenv"),
        ("azure.identity", "azure-identity"),
        ("azure.ai.projects", "azure-ai-projects"),
        ("pydantic", "pydantic"),
    ]
    
    all_installed = True
    for module, package in required:
        try:
            __import__(module)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} not installed. Run: pip install {package}")
            all_installed = False
    
    return all_installed


def check_env_file():
    """Check .env file exists and has required variables."""
    from pathlib import Path
    
    env_path = Path(__file__).parent.parent / ".env"
    
    if not env_path.exists():
        print("⚠️  .env file not found. Copy .env.example to .env and add your credentials.")
        return False
    
    # Load env file
    from dotenv import load_dotenv
    load_dotenv(env_path)
    
    # Check for connection string OR individual settings
    conn_string = os.getenv("AZURE_AI_PROJECT_CONNECTION_STRING")
    subscription = os.getenv("AZURE_SUBSCRIPTION_ID")
    
    if conn_string and not conn_string.startswith("your-"):
        masked = conn_string[:20] + "..." if len(conn_string) > 20 else "***"
        print(f"✅ AZURE_AI_PROJECT_CONNECTION_STRING = {masked}")
        return True
    elif subscription:
        print(f"✅ Using individual Azure settings (subscription: {subscription[:8]}...)")
        return True
    else:
        print("⚠️  No Azure credentials configured in .env")
        print("   Set AZURE_AI_PROJECT_CONNECTION_STRING from ai.azure.com")
        print("   (Project settings → Project properties → Project connection string)")
        return False


def check_azure_auth():
    """Test Azure authentication (optional, requires network)."""
    try:
        from azure.identity import DefaultAzureCredential
        credential = DefaultAzureCredential()
        # Just verify it can be created, don't actually authenticate
        print("✅ Azure DefaultAzureCredential available")
        return True
    except Exception as e:
        print(f"⚠️  Azure authentication may need setup: {e}")
        print("   Run 'az login' or configure environment credentials")
        return False


def main():
    """Run all setup verification checks."""
    print("\n🔍 Verifying your setup...\n")
    print("=" * 50)
    
    print("\n📦 Python Version:")
    python_ok = check_python_version()
    
    print("\n📚 Dependencies:")
    deps_ok = check_dependencies()
    
    print("\n🔐 Environment Variables:")
    env_ok = check_env_file()
    
    print("\n🔑 Azure Authentication:")
    auth_ok = check_azure_auth()
    
    print("\n" + "=" * 50)
    
    if python_ok and deps_ok and env_ok:
        print("\n✅ Setup verified! You're ready to build agents.\n")
        return 0
    elif python_ok and deps_ok:
        print("\n⚠️  Core setup OK, but credentials need configuration.")
        print("   Follow Step 4 in the README to set up Azure credentials.\n")
        return 0
    else:
        print("\n❌ Some checks failed. Please resolve the issues above.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
