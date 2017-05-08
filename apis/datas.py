import requests
import urllib3
import rat

from bs4 import BeautifulSoup
json={
  "location": {
    "entity_type": "",
    "entity_id": 0,
    "title": "Sector 127",
    "latitude": "28.5341940000",
    "longitude": "77.3464090000",
    "city_id": 1,
    "city_name": "Delhi NCR",
    "country_id": 1,
    "country_name": "India"
  },
  "popularity": {
    "popularity": "2.43",
    "nightlife_index": "0.04",
    "nearby_res": [
      "18222558",
      "309061",
      "7941",
      "5616",
      "310246",
      "18245276",
      "18244258",
      "311541",
      "18448813"
    ],
    "top_cuisines": [
      "North Indian",
      "Chinese",
      "Fast Food",
      "Cafe",
      "Mughlai"
    ],
    "popularity_res": "100",
    "nightlife_res": "10",
    "subzone": "Sector 127, Noida",
    "subzone_id": 667,
    "city": "Delhi NCR"
  },
  "link": "https://www.zomato.com/ncr/sector-127-noida-restaurants",
  "nearby_restaurants": [
    {
      "restaurant": {
        "R": {
          "res_id": 18222558
        },
        "apikey": "d2b8fadf3bf0af49c59eee82826c755b",
        "id": "18222558",
        "name": "Cafe Pathshala",
        "url": "https://www.zomato.com/ncr/cafe-pathshala-sector-125-noida?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "location": {
          "address": "KO-12, Near Amity University, Sector 126, Near Sector 125, Noida",
          "locality": "Sector 125",
          "city": "Noida",
          "city_id": 1,
          "latitude": "28.5418572000",
          "longitude": "77.3347308000",
          "zipcode": "",
          "country_id": 1,
          "locality_verbose": "Sector 125, Noida"
        },
        "switch_to_order_menu": 0,
        "cuisines": "Cafe, Italian, Continental, Chinese",
        "average_cost_for_two": 550,
        "price_range": 2,
        "currency": "Rs.",
        "offers": [],
        "thumb": "https://b.zmtcdn.com/data/pictures/8/18222558/08847b086c317aeff9dc5cf7d65d81d4_featured_v2.jpg",
        "user_rating": {
          "aggregate_rating": "3.8",
          "rating_text": "Good",
          "rating_color": "9ACD32",
          "votes": "233"
        },
        "photos_url": "https://www.zomato.com/ncr/cafe-pathshala-sector-125-noida/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
        "menu_url": "https://www.zomato.com/ncr/cafe-pathshala-sector-125-noida/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
        "featured_image": "https://b.zmtcdn.com/data/pictures/8/18222558/08847b086c317aeff9dc5cf7d65d81d4_featured_v2.jpg",
        "has_online_delivery": 1,
        "is_delivering_now": 1,
        "deeplink": "zomato://restaurant/18222558",
        "order_url": "https://www.zomato.com/ncr/cafe-pathshala-sector-125-noida/order?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "order_deeplink": "",
        "has_table_booking": 0,
        "events_url": "https://www.zomato.com/ncr/cafe-pathshala-sector-125-noida/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"
      }
    },
    {
      "restaurant": {
        "R": {
          "res_id": 309061
        },
        "apikey": "d2b8fadf3bf0af49c59eee82826c755b",
        "id": "309061",
        "name": "Flavor Pirates",
        "url": "https://www.zomato.com/ncr/flavor-pirates-sector-127-noida?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "location": {
          "address": "Plot 7, IHDP Business Park, Sector 127, Noida",
          "locality": "Sector 127",
          "city": "Noida",
          "city_id": 1,
          "latitude": "28.5347031000",
          "longitude": "77.3477866000",
          "zipcode": "",
          "country_id": 1,
          "locality_verbose": "Sector 127, Noida"
        },
        "switch_to_order_menu": 0,
        "cuisines": "North Indian, Mughlai, Chinese",
        "average_cost_for_two": 900,
        "price_range": 2,
        "currency": "Rs.",
        "offers": [],
        "thumb": "https://b.zmtcdn.com/data/pictures/1/309061/65c2c6f6617980bbe48590c353d54228_featured_v2.jpg",
        "user_rating": {
          "aggregate_rating": "2.5",
          "rating_text": "Average",
          "rating_color": "FFBA00",
          "votes": "156"
        },
        "photos_url": "https://www.zomato.com/ncr/flavor-pirates-sector-127-noida/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
        "menu_url": "https://www.zomato.com/ncr/flavor-pirates-sector-127-noida/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
        "featured_image": "https://b.zmtcdn.com/data/pictures/1/309061/65c2c6f6617980bbe48590c353d54228_featured_v2.jpg",
        "has_online_delivery": 1,
        "is_delivering_now": 1,
        "deeplink": "zomato://restaurant/309061",
        "order_url": "https://www.zomato.com/ncr/flavor-pirates-sector-127-noida/order?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "order_deeplink": "",
        "has_table_booking": 1,
        "book_url": "https://www.zomato.com/ncr/flavor-pirates-sector-127-noida/book?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "events_url": "https://www.zomato.com/ncr/flavor-pirates-sector-127-noida/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"
      }
    },
    {
      "restaurant": {
        "R": {
          "res_id": 7941
        },
        "apikey": "d2b8fadf3bf0af49c59eee82826c755b",
        "id": "7941",
        "name": "Foodfellas",
        "url": "https://www.zomato.com/ncr/foodfellas-sector-127-noida?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "location": {
          "address": "Plot 2B, Noida Express Way, Sector 127, Noida",
          "locality": "Sector 127",
          "city": "Noida",
          "city_id": 1,
          "latitude": "28.5399941000",
          "longitude": "77.3444050000",
          "zipcode": "0",
          "country_id": 1,
          "locality_verbose": "Sector 127, Noida"
        },
        "switch_to_order_menu": 0,
        "cuisines": "North Indian, Chinese, Fast Food",
        "average_cost_for_two": 700,
        "price_range": 2,
        "currency": "Rs.",
        "offers": [],
        "thumb": "https://b.zmtcdn.com/data/pictures/1/7941/3d105b25a5abc26f9f3c32a88c813add_featured_v2.jpg",
        "user_rating": {
          "aggregate_rating": "3.3",
          "rating_text": "Average",
          "rating_color": "CDD614",
          "votes": "87"
        },
        "photos_url": "https://www.zomato.com/ncr/foodfellas-sector-127-noida/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
        "menu_url": "https://www.zomato.com/ncr/foodfellas-sector-127-noida/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
        "featured_image": "https://b.zmtcdn.com/data/pictures/1/7941/3d105b25a5abc26f9f3c32a88c813add_featured_v2.jpg",
        "has_online_delivery": 1,
        "is_delivering_now": 0,
        "deeplink": "zomato://restaurant/7941",
        "has_table_booking": 1,
        "book_url": "https://www.zomato.com/ncr/foodfellas-sector-127-noida/book?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "events_url": "https://www.zomato.com/ncr/foodfellas-sector-127-noida/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"
      }
    },
    {
      "restaurant": {
        "R": {
          "res_id": 5616
        },
        "apikey": "d2b8fadf3bf0af49c59eee82826c755b",
        "id": "5616",
        "name": "Subway",
        "url": "https://www.zomato.com/ncr/subway-sector-127-noida?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "location": {
          "address": "Ground Floor, Tower B, Logic Techno Park, Sector 127, Noida",
          "locality": "Sector 127",
          "city": "Noida",
          "city_id": 1,
          "latitude": "28.5359520000",
          "longitude": "77.3458126000",
          "zipcode": "0",
          "country_id": 1,
          "locality_verbose": "Sector 127, Noida"
        },
        "switch_to_order_menu": 0,
        "cuisines": "American, Fast Food, Salad, Healthy Food",
        "average_cost_for_two": 500,
        "price_range": 2,
        "currency": "Rs.",
        "offers": [],
        "thumb": "https://b.zmtcdn.com/data/pictures/chains/7/147/3d38dc0bcbaf17478cd86ef822f53947_featured_v2.jpg",
        "user_rating": {
          "aggregate_rating": "2.2",
          "rating_text": "Poor",
          "rating_color": "FF7800",
          "votes": "69"
        },
        "photos_url": "https://www.zomato.com/ncr/subway-sector-127-noida/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
        "menu_url": "https://www.zomato.com/ncr/subway-sector-127-noida/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
        "featured_image": "https://b.zmtcdn.com/data/pictures/chains/7/147/3d38dc0bcbaf17478cd86ef822f53947_featured_v2.jpg",
        "has_online_delivery": 1,
        "is_delivering_now": 1,
        "deeplink": "zomato://restaurant/5616",
        "order_url": "https://www.zomato.com/ncr/subway-sector-127-noida/order?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "order_deeplink": "",
        "has_table_booking": 0,
        "events_url": "https://www.zomato.com/ncr/subway-sector-127-noida/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"
      }
    },
    {
      "restaurant": {
        "R": {
          "res_id": 310246
        },
        "apikey": "d2b8fadf3bf0af49c59eee82826c755b",
        "id": "310246",
        "name": "Get Grubs",
        "url": "https://www.zomato.com/ncr/get-grubs-sector-127-noida?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "location": {
          "address": "Tower A, Tech Boulevard, Plot 6, Sector 127, Noida",
          "locality": "Sector 127",
          "city": "Noida",
          "city_id": 1,
          "latitude": "28.5356372000",
          "longitude": "77.3467547000",
          "zipcode": "",
          "country_id": 1,
          "locality_verbose": "Sector 127, Noida"
        },
        "switch_to_order_menu": 0,
        "cuisines": "Fast Food, Burger",
        "average_cost_for_two": 250,
        "price_range": 1,
        "currency": "Rs.",
        "offers": [],
        "thumb": "https://b.zmtcdn.com/data/pictures/6/310246/202d1c605a8d2eae02c22908613b3fb0_featured_v2.jpg",
        "user_rating": {
          "aggregate_rating": "3.6",
          "rating_text": "Good",
          "rating_color": "9ACD32",
          "votes": "81"
        },
        "photos_url": "https://www.zomato.com/ncr/get-grubs-sector-127-noida/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
        "menu_url": "https://www.zomato.com/ncr/get-grubs-sector-127-noida/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
        "featured_image": "https://b.zmtcdn.com/data/pictures/6/310246/202d1c605a8d2eae02c22908613b3fb0_featured_v2.jpg",
        "has_online_delivery": 1,
        "is_delivering_now": 1,
        "deeplink": "zomato://restaurant/310246",
        "order_url": "https://www.zomato.com/ncr/get-grubs-sector-127-noida/order?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "order_deeplink": "",
        "has_table_booking": 0,
        "events_url": "https://www.zomato.com/ncr/get-grubs-sector-127-noida/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"
      }
    },
    {
      "restaurant": {
        "R": {
          "res_id": 18245276
        },
        "apikey": "d2b8fadf3bf0af49c59eee82826c755b",
        "id": "18245276",
        "name": "Laser Wars Lounge",
        "url": "https://www.zomato.com/ncr/laser-wars-lounge-sector-127-noida?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "location": {
          "address": "KO-17, Opposite Amity Gate-2, Sector 127, Noida",
          "locality": "Sector 127",
          "city": "Noida",
          "city_id": 1,
          "latitude": "28.5417097000",
          "longitude": "77.3344804000",
          "zipcode": "201303",
          "country_id": 1,
          "locality_verbose": "Sector 127, Noida"
        },
        "switch_to_order_menu": 0,
        "cuisines": "Fast Food",
        "average_cost_for_two": 500,
        "price_range": 2,
        "currency": "Rs.",
        "offers": [],
        "thumb": "https://b.zmtcdn.com/data/pictures/6/18245276/d0efd3e680012b802128c63841fde8fc_featured_v2.jpg",
        "user_rating": {
          "aggregate_rating": "3.3",
          "rating_text": "Average",
          "rating_color": "CDD614",
          "votes": "51"
        },
        "photos_url": "https://www.zomato.com/ncr/laser-wars-lounge-sector-127-noida/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
        "menu_url": "https://www.zomato.com/ncr/laser-wars-lounge-sector-127-noida/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
        "featured_image": "https://b.zmtcdn.com/data/pictures/6/18245276/d0efd3e680012b802128c63841fde8fc_featured_v2.jpg",
        "has_online_delivery": 0,
        "is_delivering_now": 0,
        "deeplink": "zomato://restaurant/18245276",
        "has_table_booking": 0,
        "events_url": "https://www.zomato.com/ncr/laser-wars-lounge-sector-127-noida/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"
      }
    },
    {
      "restaurant": {
        "R": {
          "res_id": 18244258
        },
        "apikey": "d2b8fadf3bf0af49c59eee82826c755b",
        "id": "18244258",
        "name": "Fudroo.com",
        "url": "https://www.zomato.com/fudroo-com?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "location": {
          "address": "Sector 127, Noida",
          "locality": "Sector 127",
          "city": "Noida",
          "city_id": 1,
          "latitude": "28.5357736000",
          "longitude": "77.3510898000",
          "zipcode": "",
          "country_id": 1,
          "locality_verbose": "Sector 127, Noida"
        },
        "switch_to_order_menu": 0,
        "cuisines": "North Indian, South Indian, Chinese",
        "average_cost_for_two": 400,
        "price_range": 1,
        "currency": "Rs.",
        "offers": [],
        "thumb": "https://b.zmtcdn.com/data/pictures/8/18244258/f45f188a434131ebe46fae86d74d5ea1_featured_v2.JPG",
        "user_rating": {
          "aggregate_rating": "3.4",
          "rating_text": "Average",
          "rating_color": "CDD614",
          "votes": "39"
        },
        "photos_url": "https://www.zomato.com/fudroo-com/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
        "menu_url": "https://www.zomato.com/fudroo-com/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
        "featured_image": "https://b.zmtcdn.com/data/pictures/8/18244258/f45f188a434131ebe46fae86d74d5ea1_featured_v2.JPG",
        "has_online_delivery": 0,
        "is_delivering_now": 0,
        "deeplink": "zomato://restaurant/18244258",
        "has_table_booking": 0,
        "events_url": "https://www.zomato.com/fudroo-com/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"
      }
    },
    {
      "restaurant": {
        "R": {
          "res_id": 311541
        },
        "apikey": "d2b8fadf3bf0af49c59eee82826c755b",
        "id": "311541",
        "name": "Churli",
        "url": "https://www.zomato.com/ncr/churli-sector-125-noida?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "location": {
          "address": "RA-11, Opposite Gate 2A, Amity University, Sector 126, Near Sector 125, Noida",
          "locality": "Sector 125",
          "city": "Noida",
          "city_id": 1,
          "latitude": "28.5424960000",
          "longitude": "77.3355364000",
          "zipcode": "",
          "country_id": 1,
          "locality_verbose": "Sector 125, Noida"
        },
        "switch_to_order_menu": 0,
        "cuisines": "North Indian, Fast Food, South Indian",
        "average_cost_for_two": 550,
        "price_range": 2,
        "currency": "Rs.",
        "offers": [],
        "zomato_events": [
          {
            "event": {
              "event_id": 88189,
              "friendly_start_date": "11 November, 2016",
              "friendly_end_date": "30 November",
              "start_date": "2016-11-11",
              "end_date": "2017-11-30",
              "end_time": "16:00:00",
              "start_time": "12:00:00",
              "is_active": 1,
              "date_added": "2016-11-11 14:31:39",
              "photos": [
                {
                  "photo": {
                    "url": "https://b.zmtcdn.com/data/zomato_events/photos/ee0/cf4cfa9985c716d32a08186dd27fdee0_1478854899.jpg",
                    "thumb_url": "https://b.zmtcdn.com/data/zomato_events/photos/ee0/cf4cfa9985c716d32a08186dd27fdee0_1478854899.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A",
                    "order": 0,
                    "md5sum": "cf4cfa9985c716d32a08186dd27fdee0",
                    "photo_id": 145928,
                    "uuid": 54894535321,
                    "type": "FEATURED"
                  }
                }
              ],
              "restaurants": [],
              "is_valid": 1,
              "share_url": "http://www.zoma.to/r/311541",
              "title": "Special Arrangement for Farm House Parties!",
              "description": "Birthday party, Corporate Party, Theme Party, call for further details.",
              "display_time": "12:00 pm - 04:00 pm",
              "display_date": "11 November - 30 November",
              "is_end_time_set": 1,
              "disclaimer": "Restaurants are solely responsible for the service; availability and quality of the events including all or any cancellations/ modifications/ complaints.",
              "event_category": 1,
              "event_category_name": "",
              "book_link": ""
            }
          }
        ],
        "thumb": "https://b.zmtcdn.com/data/pictures/1/311541/3b09d7b039b9437f484c5289269c5d43_featured_v2.jpg",
        "user_rating": {
          "aggregate_rating": "3.2",
          "rating_text": "Average",
          "rating_color": "CDD614",
          "votes": "42"
        },
        "photos_url": "https://www.zomato.com/ncr/churli-sector-125-noida/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
        "menu_url": "https://www.zomato.com/ncr/churli-sector-125-noida/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
        "featured_image": "https://b.zmtcdn.com/data/pictures/1/311541/3b09d7b039b9437f484c5289269c5d43_featured_v2.jpg",
        "has_online_delivery": 0,
        "is_delivering_now": 0,
        "deeplink": "zomato://restaurant/311541",
        "has_table_booking": 0,
        "events_url": "https://www.zomato.com/ncr/churli-sector-125-noida/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"
      }
    },
    {
      "restaurant": {
        "R": {
          "res_id": 18448813
        },
        "apikey": "d2b8fadf3bf0af49c59eee82826c755b",
        "id": "18448813",
        "name": "Cut The Crepe",
        "url": "https://www.zomato.com/ncr/cut-the-crepe-sector-125-noida?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "location": {
          "address": "Near Amity University, Sector 125, Noida",
          "locality": "Sector 125",
          "city": "Noida",
          "city_id": 1,
          "latitude": "28.5414647000",
          "longitude": "77.3343718000",
          "zipcode": "",
          "country_id": 1,
          "locality_verbose": "Sector 125, Noida"
        },
        "switch_to_order_menu": 0,
        "cuisines": "Cafe",
        "average_cost_for_two": 500,
        "price_range": 2,
        "currency": "Rs.",
        "offers": [],
        "thumb": "",
        "user_rating": {
          "aggregate_rating": "3.4",
          "rating_text": "Average",
          "rating_color": "CDD614",
          "votes": "16"
        },
        "photos_url": "https://www.zomato.com/ncr/cut-the-crepe-sector-125-noida/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
        "menu_url": "https://www.zomato.com/ncr/cut-the-crepe-sector-125-noida/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
        "featured_image": "",
        "has_online_delivery": 0,
        "is_delivering_now": 0,
        "deeplink": "zomato://restaurant/18448813",
        "has_table_booking": 0,
        "events_url": "https://www.zomato.com/ncr/cut-the-crepe-sector-125-noida/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"
      }
    }
  ]
}

nr=json["nearby_restaurants"]
for i in nr:
  adr=(i["restaurant"]["location"]["address"])
  rid=(i["restaurant"]["R"]['res_id'])
  rname=(i["restaurant"]["name"])
  print (adr)
  print (rid)
  print (rname)
  response = requests.get("https://developers.zomato.com/api/v2.1/reviews?res_id=+"+str(rid), headers={"user_key": "d2b8fadf3bf0af49c59eee82826c755b", "Accept": "application/json"})
  soup = BeautifulSoup(response.content, "html.parser")
  print (soup)