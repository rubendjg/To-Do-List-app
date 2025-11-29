# 📄 REPORT.md — Improvements Implemented (Rewritten Summary)

This report provides a structured overview of the improvements introduced in the updated version of the To-Do List application. The enhancements focus on user security, data integrity, error handling, and code maintainability. Each improvement addresses limitations identified in the previous version and contributes to a more secure and reliable user experience.

---

## **2.1 Strengthened User Authentication & Session Security**
The earlier implementation allowed users to access other users’ accounts by manually modifying the user ID in the URL. This was a critical security vulnerability. The authentication system has now been fortified by ensuring that:
- A user's ID is stored in the session upon login or signup.
- Any request involving user-specific content verifies that the ID in the URL matches the ID stored in the session.
- When mismatches occur, the user is redirected to the application's home page, preventing unauthorized access.

**Outcome:**  
Users can no longer view, modify, or access another user's data simply by altering the URL, thereby closing a major security loophole.

---

## **2.2 Secure Account Deletion with Password Confirmation**
Because account deletion is permanent, an additional layer of protection was added to prevent accidental or malicious deletion.

The system now requires:
- The user to re-enter their password before an account can be deleted.
- Verification that the provided password matches the stored password.

**Outcome:**  
This ensures that only the legitimate account owner can initiate deletion and reduces the risk of accidental data loss.

---

## **2.3 User Data Modification Enhancements**
Users are able to update their usernames and passwords. Currently, the system does not require the user to enter their existing password before making changes—acceptable for early development but not ideal for production.

**Planned future improvements include:**
- Email-based verification.
- Password reset and account recovery mechanisms.
- Two-factor authentication (2FA) for added security.

**Outcome:**  
The current implementation provides basic functionality while maintaining a roadmap for transitioning to industry-standard security practices.

---

## **2.4 Improved Error Handling & User Feedback**
The user experience surrounding authentication has been made more informative and user-friendly.

Enhancements include:
- Clear error messages when incorrect login credentials are entered.
- Feedback when a username is already in use during account creation.

**Outcome:**  
Users receive immediate, actionable feedback when something goes wrong, reducing confusion and improving overall usability.

---

## **2.5 Refactoring for Cleaner & More Maintainable Code**
The previous codebase contained significant duplication, especially in task-related views for completed and uncompleted tasks.

Refactoring efforts included:
- Consolidating repeated logic into unified functions.
- Introducing a `next` parameter to handle navigation flows more elegantly.
- Using `next` to determine where the user should be redirected after actions such as editing or deleting tasks and when returning from the account settings page.

**Outcome:**  
The code is now more concise, readable, and maintainable. Future updates will be easier to implement and less error‑prone.

---

If you want, I can expand this report with diagrams, a PDF export, or a formal academic tone.

