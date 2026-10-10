# Smart Home Operations Dashboard

![Python](https://img.shields.io/badge/Python-application-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-responsive%20UI-FF4B4B?logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-local%20data-003B57?logo=sqlite&logoColor=white)
![Security](https://img.shields.io/badge/access-private%20by%20design-34D399)

## Project overview

This repository presents a privately hosted smart-home operations dashboard that brings energy, lighting, network, climate, audio, tasks and household services together in one responsive interface.

The application was designed and developed by **Ellen Rensenbrink / SiteGuardly** as a modular Python system with local-first data handling and controlled integrations.

![Smart home overview](dashboard-overview.png)

## The challenge

Connected-home products often have separate apps, authentication methods and data formats. The project turns those independent systems into one consistent experience while keeping credentials and device access private.

The dashboard combines information and controls for:

- HomeWizard P1 energy data;
- FoxESS solar production;
- Philips Hue lighting and scenes;
- Sonos and Spotify playback;
- router, modem and internet quality monitoring;
- household tasks and shopping lists;
- cooling, waste and cleaning workflows;
- system health, backups and maintenance.

## Architecture

```mermaid
flowchart TD
    A[Devices & cloud APIs] --> B[Typed integration clients]
    B --> C[Service layer]
    C --> D[(Local SQLite storage)]
    C --> E[Automation workers]
    D --> F[Responsive dashboard]
    E --> G[Health & watchdog checks]
    G --> F
    F --> H[Authenticated private access]
```

Integrations are isolated behind clients and services instead of being embedded directly in page code. This makes individual devices replaceable, improves testability and keeps the interface responsive when an external service is temporarily unavailable.

## Selected capabilities

- Live energy flow, solar production and consumption analysis.
- Historical period comparison, tariffs and cost calculations.
- Lighting controls, scenes and scheduled overrides.
- Speaker selection and multi-room audio controls.
- Internet quality history and local network status.
- Background collectors with heartbeat monitoring.
- Watchdog recovery for individual services.
- Validated backups and controlled restore procedures.
- Configuration change logging with sensitive-value masking.
- Desktop, tablet and mobile layouts.
- Automated unit, integration, security and visual regression tests.

## Interface examples

### System health and maintenance

The configuration area brings service health, security checks, backup controls and the change log into one operator view.

![System health](system-health.png)

### Audio integration

The music module provides a consistent interface for Spotify and Sonos devices without exposing device credentials to the browser.

![Audio integration](audio-control.png)

### Responsive layouts

The same application is optimised for desktop, tablet and phone use.

| Desktop | Tablet | Mobile |
| --- | --- | --- |
| ![Desktop layout](desktop.jpg) | ![Tablet layout](tablet.jpg) | ![Mobile layout](mobile.jpg) |

## Security and resilience

- The application is not directly exposed to the public internet.
- API keys and device credentials remain outside version control.
- Sensitive credentials are stored through the operating system credential store.
- Local access requires authentication.
- Private remote access uses an authenticated encrypted network path.
- Individual collectors can recover without restarting the entire platform.
- Backups exclude credentials and are validated before restore.

## Engineering focus

This project demonstrates experience with:

- Python and Streamlit application development;
- heterogeneous API and IoT integrations;
- resilient service and repository patterns;
- responsive interface design;
- background processes and watchdogs;
- local security and credential management;
- data modelling, SQLite and migrations;
- automated quality and visual regression testing.

## Privacy and availability

This is a **portfolio case study**. Production source code, device identifiers, network information, credentials and household data are intentionally kept private.

