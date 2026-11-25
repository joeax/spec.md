# Product Requirements Document (PRD): Web-Based Task Manager App

## 1. Objective & Vision
To build a lightweight, intuitive, web-based task manager that helps individuals organize daily activities, reduce cognitive load, and increase productivity without the bloat of enterprise project management tools.

## 2. Target Audience & Use Cases
* **Target Users:** Freelancers, students, and busy professionals seeking a simple, no-fuss personal organizer.
* **Primary Use Case:** A user logs in, quickly lists 5–10 tasks for the day, prioritizes them, and marks them complete as they work.

## 3. Scope & Functional Requirements

### Phase 1 (MVP)
* **User Authentication:** Sign up, log in, and log out via NextAuth.js Credentials Provider (email/password).
* **Task Creation:** Add a task with a title, optional description, and a due date.
* **Task Management:** Mark tasks as complete, edit task details, and delete tasks.
* **Data Persistence:** Stored entirely in browser `window.localStorage`, mapped to the NextAuth.js user ID for session isolation.
* **Theme Toggle:** Persistent, globally accessible dark mode/light mode switch using Tailwind CSS classes.

### Phase 2 (Future Scope)
* Database migration (PostgreSQL via Prisma ORM).
* Recurring tasks (daily/weekly/monthly).
* Task categorization using custom color-coded tags.

## 4. Technical Stack & Deployment Architecture
* **Frontend Framework:** Next.js (React) App Router.
* **Styling Engine:** Tailwind CSS (Slate/Zinc palette).
* **Authentication:** NextAuth.js (JWT-based client sessions).
* **Persistence Layer:** Browser `localStorage` (MVP constraint).
* **Hosting Platform:** Vercel (Edge network, automated preview/production pipelines via GitHub).

## 5. Non-Functional Requirements
* **Performance:** Page load time under 2 seconds on the Vercel CDN.
* **Responsiveness:** Fluid grid design across mobile and desktop.
* **Theme Persistence:** Pre-render handling to eliminate dark mode flickering during client-side hydration.

---

# Next.js Boilerplate Project Structure

Below is the production-ready directory layout for this specific MVP stack using the Next.js App Router, Tailwind CSS, and NextAuth.js:

```text
task-manager-app/
├── public/
│   ├── favicon.ico
│   └── globals.css
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   └── auth/
│   │   │       └── [...nextauth]/
│   │   │           └── route.ts       # NextAuth.js API route handler
│   │   │   ├── dashboard/
│   │   │   │   └── page.ts            # Main task dashboard page
│   │   │   ├── login/
│   │   │   │   └── page.ts            # Authentication page
│   │   │   ├── layout.tsx             # Root layout with ThemeProvider wrapper
│   │   │   └── page.tsx               # Entry router / landing redirect
│   │   ├── components/
│   │   │   ├── Dashboard.tsx          # Wrapper for the task view
│   │   │   ├── TaskForm.tsx           # Simple input form for new tasks
│   │   │   ├── TaskItem.tsx           # Individual task line item with checkbox
│   │   │   ├── ThemeToggle.tsx        # Light/Dark mode utility switch
│   │   │   └── UI/
│   │   │       ├── Button.tsx         # Tailwind button component
│   │   │       └── Input.tsx          # Tailwind input component
│   │   ├── context/
│   │   │   └── ThemeContext.tsx       # LocalStorage theme management provider
│   │   └── hooks/
│   │       └── useLocalStorage.ts     # Custom hook for task syncing
│   ├── middleware.ts                  # Next.js middleware to shield dashboard routes
│   ├── tailwind.config.ts             # Tailwind darkmode setup ('class' strategy)
│   ├── tsconfig.json
│   └── package.json
```
