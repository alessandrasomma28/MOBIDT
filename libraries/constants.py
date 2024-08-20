# environment variables file for the containers and their port
containerEnvPath = "./docker-files/fiware-dt-platform/.env"

# path where the data used for simulation are stored
simulationDataPath = "./SUMO/joined/data/"

simulationPath = "./SUMO/joined/"

# folder where processed traffic loops measures are stored (tipically in a one-day length)
tlPath = "./traffic_loop_dataset/"
# folder where registered devices are stored
outputPath = "./registered_devices/"

schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "dateCreated": {
      "type": "string"
    },
    "dateModified": {
      "type": "string"
    },
    "source": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "alternateName": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "dataProvider": {
      "type": "string"
    },
    "owner": {
      "type": "array",
      "items": [
        {
          "type": "string"
        },
        {
          "type": "string"
        }
      ]
    },
    "seeAlso": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "location": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "coordinates": {
          "type": "array",
          "items": [
            {
              "type": "number"
            },
            {
              "type": "number"
            }
          ]
        }
      },
      "required": [
        "type",
        "coordinates"
      ]
    },
    "address": {
      "type": "object",
      "properties": {
        "streetAddress": {
          "type": "string"
        },
        "addressLocality": {
          "type": "string"
        },
        "addressRegion": {
          "type": "string"
        },
        "addressCountry": {
          "type": "string"
        },
        "postalCode": {
          "type": "string"
        },
        "postOfficeBoxNumber": {
          "type": "string"
        },
        "streetNr": {
          "type": "string"
        },
        "district": {
          "type": "string"
        }
      }
    },
    "areaServed": {
      "type": "string"
    },
    "type": {
      "type": "string"
    },
    "laneId": {
      "type": "integer"
    },
    "refRoadSegment": {
      "type": "string"
    },
    "dateObserved": {
      "type": "string"
    },
    "dateObservedFrom": {
      "type": "string"
    },
    "dateObservedTo": {
      "type": "string"
    },
    "intensity": {
      "type": "number"
    },
    "occupancy": {
      "type": "number"
    },
    "averageVehicleSpeed": {
      "type": "number"
    },
    "averageVehicleLength": {
      "type": "number"
    },
    "averageGapDistance": {
      "type": "number"
    },
    "congested": {
      "type": "boolean"
    },
    "averageHeadwayTime": {
      "type": "number"
    },
    "laneDirection": {
      "type": "string"
    },
    "reversedLane": {
      "type": "boolean"
    },
    "vehicleType": {
      "type": "string"
    },
    "vehicleSubType": {
      "type": "string"
    },
    "@context": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    }
  },
  "required": [
    "id",
    "type",
    "dateObserved"
  ]
}
