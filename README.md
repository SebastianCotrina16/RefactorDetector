# RefactorDetector

## Overview
`RefactorDetector` is a Docker container tailored for analyzing software projects and generating graphs that depict the cyclomatic complexity versus code churn. These visuals are paramount for pinpointing areas of the codebase that might require refactoring due to high complexity and frequent changes, potentially indicating a heightened risk of defects.

## Key Features
- Cyclomatic complexity analysis of source codes.
- Code churn evaluation through version control.
- Generation of visuals correlating cyclomatic complexity with code churn.
- Ease of use via Docker containers for environment portability and consistency.

## Prerequisites
- [Docker](https://www.docker.com/get-started): Please ensure you have Docker installed on your system.

## How to Use
You don't need to clone any repository or build images; the Docker container is available on Docker Hub. First, pull the image using the following command:

```sh
docker pull sebastiancotrina/refactordetector
```
Then, on the root of the project you want to analyze, run:
```sh
docker run --name refactordetector -v "${PWD}:/project" -it sebastiancotrina/refactordetector:latest /bin/bash
```
This command runs the container, starts a bash session, and mounts your current directory (`${PWD}`) to the container's `/project` directory for analysis.

Once you're inside the container's bash session, execute the following command to start the analysis:
```sh
./../entrypoint.sh
```
This script initiates the RefactorDetector analysis. Wait for the script to complete its execution; it will analyze the source code in the `/project` directory, calculate the cyclomatic complexity and code churn, and then generate the corresponding graph.

After the script finishes, you can find the results within the container. If you need to copy the results from the container to your host machine firs exit the container:
```sh
exit
```
Then, on your terminal where you want to copy the image:
```sh
docker cp refactordetector:/app/complexity_vs_churn.png .
```

## Contributing
Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Sebastian Cotrina – sebastiancotrina16@gmail.com

Project Link: [https://github.com/SebastianCotrina16/RefactorDetector](https://github.com/SebastianCotrina16/RefactorDetector)