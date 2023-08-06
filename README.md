# Plant Diseases Detection

This repository contains a Plant Diseases Detection project with separate models for detecting diseases in Potato, Tomato, Grape, and Corn plants based on their leaves' images. Additionally, it includes a Python Flask web application (`app.py`) and HTML templates for testing the models interactively.

## Description

The Plant Diseases Detection project aims to develop an intelligent system that can accurately identify diseases in plants based on images of their leaves. It provides separate machine learning models for detecting diseases in four different crops: Potato, Tomato, Grape, and Corn. The models are trained on a diverse dataset of plant images, including both healthy and diseased plants, and they use deep learning techniques to classify the images into healthy or diseased categories.

## Dataset

The dataset used to train the models can be found on Kaggle: [Plant Disease Expert Dataset](https://www.kaggle.com/datasets/sadmansakibmahi/plant-disease-expert)

This dataset contains images of plant leaves with labels indicating whether the plant is healthy or diseased, along with the corresponding plant species (e.g., Potato, Tomato, Grape, or Corn). The dataset is suitable for training machine learning models to detect plant diseases based on leaf images.

Please make sure to review and comply with the dataset's license and terms of use before using it for your project.

## Project Structure

The project is organized as follows:

1. `potato_model/`: Contains the Python script and model for detecting diseases in Potato plants.
2. `tomato_model/`: Contains the Python script and model for detecting diseases in Tomato plants.
3. `grape_model/`: Contains the Python script and model for detecting diseases in Grape plants.
4. `corn_model/`: Contains the Python script and model for detecting diseases in Corn plants.
5. `app.py`: The Python Flask web application that serves as the user interface for testing the models.
6. `templates/`: Contains the HTML templates for the web application.
7. `static/`: Contains static files (CSS, images) for the web application.

## How to Use

1. Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/moaazosman/plant-diseases-detection.git
```

2. Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

3. Run the Flask web application:

```bash
python app.py
```

4. Open your web browser and go to `http://localhost:5000` to access the Plant Diseases Detection web application.

## Testing the Models

1. Upload an image of a Potato leaf, Tomato leaf, Grape leaf, or Corn leaf using the web interface.

2. The web application will process the image using the corresponding model and display the prediction result, indicating whether the leaf is healthy or diseased.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Contributions to the project are welcome! If you find any issues or want to improve the models or web application, feel free to open a pull request.

## Contact

If you have any questions or suggestions, please feel free to reach out to moaazos9137@yahoo.com.

