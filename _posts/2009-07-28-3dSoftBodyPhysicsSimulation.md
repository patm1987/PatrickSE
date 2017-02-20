---
layout: post
title: "3D Soft Body Physics Simulation"
tags: DigiPen Physics
---
This is my Phy350 final project, a soft body simulation using a simulation of the pressure force. The surface of the object is represented as a mesh of springs, and the 3D shape is created and maintained via air pressure.

Soft body objects use the Runge-Kutta 4 interpolation technique to compute motion. The pressure force is quickly and accurately computed on a per-frame basis using a linear time algorithm. Rigid body objects use an impulse based simulation and the Euler-Cromer integrator.

The physics and graphics engines used in this simulation are written in native C++. A managed C++ shim is used to expose a minimal subset of the underlying simulation to C# and other .NET languages. The frontend user interface is written in C#.

[Soft Body Physics – Program and Paper]({{ site.github.url }}/assets/digipen/3d_soft_body_physics_simulation/SoftBodySimulator.zip)

![Real Time Soft Body Simulation Using an Approximation of the Pressure Force]({{ site.github.url }}/assets/digipen/3d_soft_body_physics_simulation/Real-Time-Soft-Body-Simulation-Using-an-Approximation-of-the-Pressure-Force.pdf)

![]({{ side.github.url }}/assets/digipen/3d_soft_body_physics_simulation/soft7)
![]({{ side.github.url }}/assets/digipen/3d_soft_body_physics_simulation/soft1)
![]({{ side.github.url }}/assets/digipen/3d_soft_body_physics_simulation/soft2)
![]({{ side.github.url }}/assets/digipen/3d_soft_body_physics_simulation/soft3)
![]({{ side.github.url }}/assets/digipen/3d_soft_body_physics_simulation/soft4)
![]({{ side.github.url }}/assets/digipen/3d_soft_body_physics_simulation/soft5)
![]({{ side.github.url }}/assets/digipen/3d_soft_body_physics_simulation/soft6)

All content (c) 2009 DigiPen (USA) Corporation, all rights reserved.