# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

FocusTime is a React Native mobile application built with Expo that helps users track and manage focus sessions on specific tasks. The app includes a countdown timer, progress tracking, and a history of completed focus sessions.

## Development Commands

### Setup and Running
- `npm install` - Install dependencies
- `npm start` - Start the Expo development server
- `npm run android` - Run on Android emulator/device
- `npm run ios` - Run on iOS simulator/device
- `npm run web` - Run in web browser

No formal test or build commands are currently configured in the project.

## Architecture Overview

### Application State Flow
The application uses React hooks for state management at the app level (App.tsx):
- `currentSubject` - Tracks the current task the user is focusing on
- `history` - Maintains a list of completed focus tasks

### Feature-Based Organization
The codebase is organized by features:

**Features (`src/features/`)**
- `Focus.tsx` - Input screen where users enter a task name and initiate a focus session
- `Timer.tsx` - Main timer view displaying the countdown, showing the current task, and providing start/pause controls
- `Timing.tsx` - Button group (5, 10, 20 minutes) for setting timer duration
- `FocusHistory.tsx` - Displays a scrollable list of previously completed focus tasks

**Components (`src/components/`)**
- `Countdown.tsx` - Reusable countdown timer component that manages the timer logic using `useRef` and `useEffect`, calculates progress, and triggers callbacks when the timer ends
- `RoundedButton.tsx` - Reusable button component with customizable size and styling

**Utilities (`src/utils/`)**
- `colors.ts` - Centralized color definitions (blue, white, progress bar colors)
- `sizes.ts` - Centralized font sizes and spacing values

### Key Component Interactions
1. User enters a task in `Focus` → `currentSubject` is set
2. App switches to `Timer` view with the selected task
3. `Countdown` component handles timer logic while `Timer` manages play/pause state and calls `useKeepAwake()` to prevent the device from sleeping
4. When timer ends, `Countdown` triggers `onEnd()` callback → task is added to `history` via App.tsx
5. User can clear the task to return to `Focus` view

### Important Implementation Details
- **Timer Pausing**: The `Countdown` component tracks pause state through the `isPaused` prop and uses `useEffect` with setInterval/clearInterval to manage the countdown
- **Progress Tracking**: Timer progress (0-1) is calculated and passed to a visual progress bar in `Timer`
- **Vibration Pattern**: When timer ends, a 3-vibration pattern is triggered on the device
- **Screen Awake**: `expo-keep-awake` hook is used in `Timer` to prevent the screen from sleeping during focus sessions
- **Known Issue**: `FocusHistory.tsx` FlatList renders without explicit keys - note the TODO comment about adding keyExtractor for better performance

### UI Framework
- Built with React Native and Expo
- Uses `react-native-paper` for UI components (TextInput)
- Uses `react-native-progress` for the progress bar
- Uses `react-native-safe-area-context` for safe area handling
- Styling is done with React Native's StyleSheet (inline styles, flexbox layout)

## TypeScript Configuration
The project uses strict TypeScript with Expo's base tsconfig. All components are properly typed with interfaces (e.g., `FocusProps`, `TimerProps`, `CountdownProps`).
