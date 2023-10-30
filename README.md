# ShapeFinder

## Introduction and Goals
A program to detect shapes and their colors in real time.
Shape, color and contours are displayed on the image/camera feed in realtime. 
A log with the previous mentioned variables is being written.


Programmed as part of the Software Engineering course in 2023.

## Context and Scope
The scope of this project is to write a small python application that uses the
livestream of a camera and performs real-time object pattern recognition and color detection.
The recognition is visualized within the livestream and the information gathered is logged into a csv file for later analysis. 

### Following:
<p>Object Pattern Recognition: The application can detect a square, a triangle, a circle and a rectangle.
<p>Color Detection: The application can detect red, green, blue, yellow and violet in their prominent variants.
<p>Real-time Visualization: Overlay recognized objects with their respective patterns and colors on the
live video/image,
Data Loggin: Log timestamps, pattern type and detected color, information is stored in a csv file.

## Solution Strategy


## Building Block View (von euch erstelltes Komponentendiagram)
```mermaid
    flowchart LR

    idCam(Camera)
    idIm(Image from file)
    idDetCol(Color Detector)
    idDetSha(Shape Detector)

    idLog(Logfile creation)
    idVis(Visualization)

    idCam & idIm -- image --> idDetSha 
    idCam & idIm -- image --> idDetCol

    idDetSha -- Shape information-->idVis & idLog
    idDetCol -- Color information-->idVis & idLog


```



## Runtime View (Ein dynamisches Sequenz Diagramm, wie die SW funktioniert)
```mermaid
    sequenceDiagram
    
    
    Read Data ->>+ color_detector: image
    Read Data ->>+ shape_detector: image
    
    shape_detector ->>+ rt_Visualize: shapes
    color_detector ->>+ rt_Visualize: colors
    color_detector ->>+ logging: colors
    shape_detector ->>+ logging: shapes

```

## Architectural Decisions 
The ShapeFinder consists of 4 classes, one for color detection one for shape detection two smaller ones, one for logging and one for rtVisualization.
They are kept separetly to have a good maintainability 

## Risks and Technical Depts


## Glossary (falls was vorkommt, was man nicht auf Anhieb versteht)
