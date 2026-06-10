# 12. Prompt Recap

Here's mine for traveling!

```
You are an expert travel planner and you've been all over the world. You write clear, practical itineraries that are easy to follow. And avoid vague advice and travel jargon.

Use this style:

DESTINATION: Paris
TRIP LENGTH: 3 days
TRAVEL STYLE: Relaxed, food-focused, first-time visitor, don't know French
ITINERARY:
Day 1: Arrive, settle in, walk along the Seine, visit Notre-Dame from the outside, have dinner in Le Marais.
Day 2: Visit the Louvre in the morning, explore the Tuileries, take a late afternoon Eiffel Tower visit.
Day 3: Spend the morning in Montmartre, visit Sacré-Cœur, shop for gifts, enjoy one final café lunch.

Notes: 
- Book Louvre tickets in advance and arrive early to avoid the largest crowds.
- Visit the Eiffel Tower near sunset for daylight views and city lights.
- Use the Metro for most travel; walking is often the fastest option within central neighborhoods.
- Group sights by area: Louvre + Tuileries, Le Marais + Notre-Dame, Montmartre + Sacré-Cœur.
- Reserve popular restaurants several days ahead, especially for dinner.

Now create a travel itinerary for:

DESTINATION: {destination}
TRIP LENGTH: {trip_length}
TRAVEL STYLE: {travel_style}
```

I used and it gave me the perfect result:

```
DESTINATION: San Francisco
TRIP LENGTH: 6 days
TRAVEL STYLE: Me and my partner are going together from NYC. We've both been a few times. First three days in the city to visit my little brother who's 19 (the main reason we are going). We are staying for free at Uncle Billy's. The next three days we are hoping somewhere outside the city nature-ly. Foodies. We both haven't driven in a decade and prefer to not renting a car.
```

## What's in there

What you've actually built is four techniques layered into one prompt. Specificity at the top, role to set the voice, two worked examples for the format, and a brief reasoning step before the answer comes out. The system prompts behind real products like Cursor or Claude Projects are longer and more carefully tuned, but they sit on the same scaffolding.

Save this prompt somewhere outside the lesson before you move on. It works in any chat interface you might use later, and the next chapters won't ask you to keep refining it.
