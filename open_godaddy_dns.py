#!/usr/bin/env python3
"""
Open GoDaddy DNS settings directly
"""

import webbrowser
import subprocess
import time

def main():
    print("🌐 Opening GoDaddy DNS Configuration")
    print("="*50)
    
    print("\n📋 Current DNS Status:")
    print("-"*40)
    
    # Check current DNS
    result = subprocess.run(
        "nslookup jaspermatters.com | grep Address | tail -2",
        shell=True, capture_output=True, text=True
    )
    print("Current IPs:", result.stdout.strip())
    
    print("\n❌ PROBLEM: DNS not pointing to Netlify!")
    print("   Current: 18.208.88.157, 98.84.224.111")
    print("   Needed:  75.2.60.5 (Netlify)")
    
    print("\n📝 What to do in GoDaddy:")
    print("-"*40)
    print("1. Sign in with your credentials")
    print("2. Click on 'jaspermatters.com' → 'DNS'")
    print("3. DELETE all existing A records")
    print("4. ADD new A record:")
    print("   • Type: A")
    print("   • Name: @")
    print("   • Value: 75.2.60.5")
    print("   • TTL: 600")
    print("5. ADD/UPDATE CNAME record:")
    print("   • Type: CNAME")
    print("   • Name: www")
    print("   • Value: ourjourney.netlify.app")
    print("   • TTL: 600")
    print("6. SAVE all changes")
    
    print("\n🚀 Opening GoDaddy in browser...")
    
    # Open GoDaddy DNS management
    url = "https://dcc.godaddy.com/control/jaspermatters.com/dns"
    webbrowser.open(url)
    
    print("\n✅ Browser opened to GoDaddy DNS")
    print("   If not logged in, go to:")
    print("   https://www.godaddy.com → Sign In → My Products")
    
    print("\n⏰ After updating DNS:")
    print("   • Changes take 1-2 hours to propagate")
    print("   • Your portfolio will automatically appear")
    print("   • No further action needed on Netlify")
    
    print("\n🔍 To verify changes (run in 1 hour):")
    print("   python3 verify_deployment.py")

if __name__ == "__main__":
    main()