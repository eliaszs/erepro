# -- FILE: features/listings.feature
Feature: Listings Service

  Scenario: Run a CreateListings test
    Given a csv file "../data/properties_clean.csv" with a list of 28 properties
    When connected to a local listings grpc server at "localhost:9090"
    When posted the list to the service
    Then the service returns 28 responses with a success code

    When queried for the list of 10 properties
    Then service will return a list of 10 properties to the user
