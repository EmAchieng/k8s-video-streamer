# Smart Video Routing for CDN Optimization

## Overview
This project uses Kubernetes to dynamically route video streams based on network conditions and viewer geolocation. It ensures uninterrupted service for live streaming platforms.


## Kubernetes Configuration
- `k8s/deployment.yaml`: Defines the deployment for the video router.
- `k8s/service.yaml`: Exposes the deployment as a service.
- `k8s/ingress.yaml`: Configures ingress for external access.

## Jenkins Pipeline
- `Jenkinsfile`: Defines the CI/CD pipeline with stages for build, test, and deploy.

## Unit Tests
- `tests/`: Contains unit tests for the application.

## How to Run
1. Build the Docker image:
    ```sh
    docker build -t video-router:latest .
    ```
2. Apply Kubernetes configurations:
    ```sh
    kubectl apply -f k8s/
    ```
3. Access the service via `localhost`. Forward the port to access the service.
```sh
kubectl port-forward service/video-router 8080:80
 ```

Open your browser and go to http://localhost:8080 to see the home page.
To test the routing, you can use a tool like curl or Postman to send a POST request to http://localhost:8080/route with a JSON body containing the IP address.

```sh
curl -X POST http://localhost:8080/route -H "Content-Type: application/json" -d '{"ip": "8.8.8.8"}'
```

## If you want to run the flask app locally without Docker
```sh
pip install flask
cd src
python main.py
```

## How to Test
Run the unit tests using pytest:
```sh
pip install pytest
pytest tests/
```

This setup includes the necessary files and folders for the project. Adjust the configurations and code as needed for your specific requirements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
