using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Planet : MonoBehaviour
{
    public float yearLengthInSeconds = 10f;
    public float parentDegreesPerSecond;
    public bool clockwiseOrbit = true;
    
    public float dayLengthInSeconds = 1f;
    public float selfDegreesPerSecond;
    public bool clockwiseSpin = true;

    [Range(0f, 1f)]
    public float innerOrbitMultiplier = 0.5f;

    private Transform _pivot;
    private bool _isParentNull;

    private float orbitalRadius;

    private void Start()
    {
        var myTransform = transform;
        var parent = myTransform.parent;
        _isParentNull = parent == null;
        _pivot = new GameObject($"{name} Pivot").transform;
        _pivot.position = (_isParentNull ? myTransform.position : myTransform.parent.position);
        _pivot.SetParent(parent);
        transform.SetParent(_pivot);
        
        foreach (Transform child in transform)
        {
            child.SetParent(_pivot);
        }

        orbitalRadius = transform.localPosition.x;
    }

    private void Update()
    {
        selfDegreesPerSecond = 360f / dayLengthInSeconds * (clockwiseSpin ? -1f : 1f);
        transform.eulerAngles += Vector3.forward * (selfDegreesPerSecond * Time.deltaTime);

        if (_isParentNull) return;

        float yearAmount = Mathf.Repeat(_pivot.eulerAngles.z, 360f) * Mathf.Deg2Rad;
        float ellipseLerp = (Mathf.Sin(yearAmount) + 1f) / 2f;
        float currentRadius = Mathf.Lerp(orbitalRadius, orbitalRadius * innerOrbitMultiplier, ellipseLerp);
        
        //Orbiting only stuff
        parentDegreesPerSecond = 360f / yearLengthInSeconds * (clockwiseOrbit ? -1f : 1f) * (ellipseLerp + 1f);
        _pivot.eulerAngles += Vector3.forward * (parentDegreesPerSecond * Time.deltaTime);
        transform.localPosition = new Vector3(
            currentRadius,
            transform.localPosition.y
        );
    }
}
