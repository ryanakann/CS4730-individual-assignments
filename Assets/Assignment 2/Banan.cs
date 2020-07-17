using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Banan : MonoBehaviour
{
    private Color _color;
    [SerializeField] private SpriteRenderer spriteRenderer;
    [SerializeField] [Range(0f, 10f)] private float cycleSpeed = 1f;
    
    // Start is called before the first frame update
    void Start()
    {
        _color = Color.white;
    }

    // Update is called once per frame
    void Update()
    {
        spriteRenderer.color = Color.HSVToRGB(Mathf.Repeat(Time.time * cycleSpeed, 1f), 1f, 1f);
    }
}
