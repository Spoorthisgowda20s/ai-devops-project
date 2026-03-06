package com.devops.aiapp;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.beans.factory.annotation.Value;
import java.util.Map;

@RestController
public class HomeController {

    @Value("${ENV:DEV}")
    private String env;

    @GetMapping("/")
    public String home() {
        return "Environment: " + env;
    }

    @GetMapping("/predict/{hours}")
    public Object predict(@PathVariable int hours) {

        String url = "http://host.docker.internal:5000/predict";

        RestTemplate restTemplate = new RestTemplate();

        Map<String,Integer> request = Map.of("hours", hours);

        return restTemplate.postForObject(url, request, Object.class);
    }
}