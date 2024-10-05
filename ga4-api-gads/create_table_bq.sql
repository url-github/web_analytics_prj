CREATE OR REPLACE TABLE `third-essence-345723.analytics_907689214.1cfdcbed2215436eb910901138e1ea84` (
    date DATE,
    googleAdsCampaignName STRING,
    googleAdsCampaignId STRING,
    keyEvents INT64,
    advertiserAdCost FLOAT64,
    advertiserAdCostPerKeyEvent FLOAT64,
    advertiserAdImpressions INT64,
    advertiserAdClicks INT64,
    advertiserAdCostPerClick FLOAT64,
    purchaseRevenue FLOAT64,
    returnOnAdSpend FLOAT64
);


bq mk --table \
third-essence-345723:analytics_907689214.1cfdcbed2215436eb910901138e1ea84 \
date:DATE,googleAdsCampaignName:STRING,googleAdsCampaignId:STRING,keyEvents:INTEGER,advertiserAdCost:FLOAT,advertiserAdCostPerKeyEvent:FLOAT,advertiserAdImpressions:INTEGER,advertiserAdClicks:INTEGER,advertiserAdCostPerClick:FLOAT,purchaseRevenue:FLOAT,returnOnAdSpend:FLOAT