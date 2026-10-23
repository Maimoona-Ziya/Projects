#A python program that estimates how risky a job or internship offer looks, analyse and rates job offers
#  or internships by asking the user about the offer and the process involved.
# The score is only an estimate. It is not proof that an offer is real or fake.

print("="*25,"OFFER ANALYSER","="*25)

#Taking user inputs about the offer they received.
print("\nAnswer these questions correctly according to the offer you received..")

score = 0

print("\n1. Did you get the offer without applying? ")
ans1 = input("\nEnter y/n for yes or no : ").lower().strip()
if ans1 == "y":
    score = score + 1

print("\n2. Did you get the offer without being interviewed? ")
ans2 = input("\nEnter y/n for yes or no : ").lower().strip()
if ans2 == "y":
    score = score + 1

print("\n3. Were you asked to pay any money (registration, training, kit, deposit)?")
ans3 = input("\nEnter y/n for yes or no : ").lower().strip()
if ans3 == "y":
    score = score + 3

print("\n4. Was the “interview” only on chat (WhatsApp or Telegram), with no call or video?")
ans4 = input("\nEnter y/n for yes or no : ").lower().strip()
if ans4 == "y":
    score = score + 2

print("\n5. Does the email use a free address like Gmail or Yahoo instead of a company domain?")
ans5 = input("\nEnter y/n for yes or no : ").lower().strip()
if ans5 == "y":
    score = score + 1

print("\n6. Are they pushing you to decide or pay quickly?")
ans6 = input("\nEnter y/n for yes or no : ").lower().strip()
if ans6 == "y":
    score = score + 2

print("\n7. Did they ask for Aadhaar, PAN, bank details or an OTP before you joined?")
ans7 = input("\nEnter y/n for yes or no : ").lower().strip()
if ans7 == "y":
    score = score + 3

print("\n8. Is the pay unusually high for the work?")
ans8 = input("\nEnter y/n for yes or no : ").lower().strip()
if ans8 == "y":
    score = score + 1

print("\n9. Can you not find the company’s official website or LinkedIn page?")
ans9 = input("\nEnter y/n for yes or no : ").lower().strip()
if ans9 == "y":
    score = score + 2

# Displaying the final scores and verdicts.
print("\n" + "=" * 20, "RESULT", "=" * 20)


print("\nRisk score:", score, "out of 16")
 
if score <= 2:
    print("Verdict: Low risk. Still verify the company before you accept.")

elif score <= 5:
    print("Verdict: Suspicious. Verify carefully before going further.")

else:
    print("Verdict: Very likely a scam. Do not pay or share documents.")


print("\nThis is only an estimate, not proof.")
print("Check the company on its official website and LinkedIn page before you pay or share documents.")


