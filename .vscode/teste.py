input int gridSpacing = 5
input double minGridDistance = 10
input double maxTakeProfitPips = 100
input double maxStopLossPips = 80
input int executionDelayMs = 10
input int runtimeSeconds = 10

class HighFrequencyTrader 
private:
    bool running;
    CRITICAL_SECTION lock;

public:
    HighFrequencyTrader() {
        running = true;
        InitializeCriticalSection(lock);
        this.ExecuteTrades();
    }

    ~HighFrequencyTrader() {
        running = false;
        DeleteCriticalSection(lock);
    }

    void ExecuteTrades() {
        while (running) {
            EnterCriticalSection(lock);

            double minPrice = RandomRange(1700, 1750);
            double maxPrice = RandomRange(1750, 1800);
            double price = RandomRange(minPrice, maxPrice);

            Print("XAU/USD Price Range: ", minPrice, " - ", maxPrice);
            Print("XAU/USD Current Price: ", price);

            double takeProfit = 30;

            for (double level = minPrice; level < maxPrice; level += gridSpacing) {
                if (price < level) {
                    takeProfit += 10;
                    takeProfit = MathMin(takeProfit, price + maxTakeProfitPips);

                    double stopLoss = MathMax(level - 10, price - 10);
                    stopLoss = MathMax(stopLoss, price - maxStopLossPips);

                    while (MathAbs(level - price) < minGridDistance) {
                        level += gridSpacing;
                    }

                    ExecuteOrder("XAUUSD", OP_BUY, 1, level, takeProfit, stopLoss);
                }