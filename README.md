<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links-->
<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

</div>

<div align="center">
  <h3 align="center">ilogger</h3>

  <p align="center">
    <i>Intelligent Logger: Benifits of no-SQL DB for storing logs and TypeDef for robust code</i>
    <br />
    <a href="https://github.com/proffapt/ilogger/issues">Request Feature | Report Bug</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
<summary>Table of Contents</summary>

- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)
- [Acknowledgements](#acknowledgments)
- [Additional documentation](#additional-documentation)

</details>


<!-- ABOUT THE PROJECT -->
## About The Project

A centralised service to store logs sent via API calls, built with Django and MonogoDB.<br> 
Then, what's special about it?
- Supports IDE suggestions (strict log type definitions)
- Extending the log type definition is just adding the definition into [ilogger_service.py](./ilogger_service.py).
- Once the type definition is updated, the checks on GET and POST request to support the newly added changes are automatically updated so you don't have to that.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To set up a local instance of the application, follow the steps below.

### Prerequisites
The following dependencies are required to be installed for the project to function properly:
* docker
* docker-compose

<p align="right">(<a href="#top">back to top</a>)</p>

### Installation

_Now that the environment has been set up and configured to properly compile and run the project, the next step is to install and configure the project locally on your system._
1. Clone the repository and cd into it
   ```sh
   git clone https://github.com/proffapt/ilogger.git
   cd ilogger/
   ```
2. Create `.env` file from `.env.example`
3. Build and start the service
   ```sh
   docker compose up --build -d
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage
<!-- UPDATE -->

Refer to [ilogger_service.example.py](./ilogger_service.example.py) for implementation of submitting / storing logs into the service. Also refer to [ilogger_service.py](./ilogger_service.py) for Log type definitions. Some key points to note:
- Supports GET, POST and DELETE requests on `/logs/api/` endpoint.
- All the fields in a log type are queryable via query-params using GET request.
- To modify the log definitions, just update the dataclasses in [ilogger_service.py](./ilogger_service.py) and you are done.


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

<p>
📫 Arpit Bhardwaj ( aka proffapt ) -
<a href="https://twitter.com/proffapt">
  <img align="center" alt="proffapt's Twitter " width="22px" src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/twitter.svg" />
</a>
<a href="https://t.me/proffapt">
  <img align="center" alt="proffapt's Telegram" width="22px" src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/telegram.svg" />
</a>
<a href="https://www.linkedin.com/in/proffapt/">
  <img align="center" alt="proffapt's LinkedIn" width="22px" src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/linkedin.svg" />
</a>
<a href="mailto:proffapt@pm.me">
  <img align="center" alt="proffapt's mail" width="22px" src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/mail.svg" />
</a>
<a href="https://cybernity.group">
  <img align="center" alt="proffapt's forum for cybernity" width="22px" src="https://cybernity.group/uploads/default/original/1X/a8338f86bbbedd39701c85d5f32cf3d817c04c27.png" />
</a>
</p>

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [Img Shields](https://shields.io)

<p align="right">(<a href="#top">back to top</a>)</p>

## Additional documentation

  - [Changelogs](/.github/CHANGELOG.md)
  - [License](/LICENSE)
  - [Security Policy](/.github/SECURITY.md)
  - [Code of Conduct](/.github/CODE_OF_CONDUCT.md)
  - [Contribution Guidelines](/.github/CONTRIBUTING.md)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/proffapt/ilogger.svg?style=for-the-badge
[contributors-url]: https://github.com/proffapt/ilogger/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/proffapt/ilogger.svg?style=for-the-badge
[forks-url]: https://github.com/proffapt/ilogger/network/members
[stars-shield]: https://img.shields.io/github/stars/proffapt/ilogger.svg?style=for-the-badge
[stars-url]: https://github.com/proffapt/ilogger/stargazers
[issues-shield]: https://img.shields.io/github/issues/proffapt/ilogger.svg?style=for-the-badge
[issues-url]: https://github.com/proffapt/ilogger/issues
[license-shield]: https://img.shields.io/github/license/proffapt/ilogger.svg?style=for-the-badge
[license-url]: https://github.com/proffapt/ilogger/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/proffapt
