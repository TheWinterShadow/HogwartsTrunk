# HogwartsTrunk

A magical Zsh theme inspired by the four Hogwarts houses, featuring rich git integration and a clean two-line prompt design.

## Overview

The Hogwarts theme is a feature-rich Zsh prompt that displays comprehensive system and git information using colors inspired by the four Hogwarts houses. It provides at-a-glance visibility of your current context, git status, and command execution results.

## Features

- **Two-line prompt design** for improved readability and command space
- **Hogwarts house colors** throughout the prompt elements
- **Git integration** with branch, status, and tracking information
- **Screen/Tmux session indicators** for terminal multiplexer users
- **Command exit status indicator** with color-coded prompt character
- **Real-time clock** showing current time

## Preview

The prompt displays information in the following format:

```
username@hostname [session] [time] ~/current/path git:branch ↑1 ↓2 ✓
❯ 
```

**First Line Components:**
- `username@hostname` - User and machine name (Gryffindor scarlet and Slytherin emerald)
- `[session]` - Active screen or tmux session (Hufflepuff gold)
- `[time]` - Current time in HH:MM:SS format (Hufflepuff gold)
- `~/current/path` - Current working directory (Ravenclaw blue)
- `git:branch` - Current git branch name (Gryffindor scarlet)
- `↑1 ↓2` - Commits ahead/behind remote (light gray)
- `✓` or `✗` - Clean (green) or dirty (red) working tree

**Second Line:**
- `❯` - Input prompt character (green for success, red for failure)

## Color Scheme

The theme uses ANSI colors inspired by Hogwarts houses:

| Element | Color | House | Code |
|---------|-------|-------|------|
| Username | Scarlet | Gryffindor | 196 |
| Hostname | Emerald | Slytherin | 34 |
| Session | Gold | Hufflepuff | 226 |
| Time | Gold | Hufflepuff | 226 |
| Path | Blue | Ravenclaw | 27 |
| Git Branch | Scarlet | Gryffindor | 196 |
| Git Status | Light Gray | - | 250 |
| Success Prompt | Green | - | 34 |
| Failure Prompt | Red | - | 196 |

## Installation

### Oh My Zsh

1. Download the theme file:
   ```bash
   curl -o ~/.oh-my-zsh/custom/themes/hogwarts.zsh-theme \
     https://raw.githubusercontent.com/YOUR_USERNAME/HogwartsTrunk/main/hogwarts.zsh-theme
   ```

2. Edit your `~/.zshrc` file and set the theme:
   ```bash
   ZSH_THEME="hogwarts"
   ```

3. Reload your Zsh configuration:
   ```bash
   source ~/.zshrc
   ```

### Manual Installation (without Oh My Zsh)

1. Download the theme file to your preferred location:
   ```bash
   mkdir -p ~/.zsh/themes
   curl -o ~/.zsh/themes/hogwarts.zsh-theme \
     https://raw.githubusercontent.com/TheWinterShadow/HogwartsTrunk/main/hogwarts.zsh-theme
   ```

2. Add to your `~/.zshrc`:
   ```bash
   source ~/.zsh/themes/hogwarts.zsh-theme
   ```

3. Reload your configuration:
   ```bash
   source ~/.zshrc
   ```

## Git Information Details

### Branch Display
Shows the current git branch name prefixed with "git:" when inside a git repository.

### Ahead/Behind Indicators
- `↑N` - Your branch is N commits ahead of the remote
- `↓N` - Your branch is N commits behind the remote
- Both indicators appear when diverged from remote

### Working Tree Status
- `✓` (green) - Clean working tree, no uncommitted changes
- `✗` (red) - Dirty working tree with uncommitted changes

### What Counts as "Dirty"
The theme checks for:
- Unstaged changes
- Staged changes
- Untracked files

## Session Indicators

The theme automatically detects and displays:
- `[screen:session_name]` - When running inside GNU Screen
- `[tmux:session_name]` - When running inside tmux

## Exit Status Indicator

The prompt character changes color based on the last command's exit status:
- Green `❯` - Previous command succeeded (exit code 0)
- Red `❯` - Previous command failed (non-zero exit code)

## Requirements

- Zsh shell
- Git (for git integration features)
- A terminal with 256-color support
- A font that supports Unicode characters (for arrows and symbols)

## Customization

You can customize the theme by editing the color variables at the top of the file:

```bash
user_color="%F{196}"       # Change username color
host_color="%F{34}"        # Change hostname color
screen_color="%F{226}"     # Change session indicator color
time_color="%F{226}"       # Change time display color
path_color="%F{27}"        # Change directory path color
git_branch_color="%F{196}" # Change git branch color
git_status_color="%F{250}" # Change ahead/behind indicator color
```

Use `%F{NUMBER}` where NUMBER is any ANSI 256 color code.

## Troubleshooting

### Symbols not displaying correctly
Ensure your terminal font supports Unicode. Recommended fonts:
- Fira Code
- JetBrains Mono
- Cascadia Code
- Any Nerd Font variant

### Git information not showing
Verify git is installed and accessible:
```bash
which git
git --version
```

### Colors appearing incorrect
Check your terminal supports 256 colors:
```bash
echo $TERM
```
Should output something like `xterm-256color` or `screen-256color`.

### Performance issues in large repositories
Git status checks can be slow in very large repositories. Consider using git sparse-checkout or adjusting git configuration:
```bash
git config core.untrackedCache true
git config core.fsmonitor true
```

## License

See the LICENSE file in the repository.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the theme.

## Credits

Inspired by the magical world of Harry Potter and the Hogwarts School of Witchcraft and Wizardry.
