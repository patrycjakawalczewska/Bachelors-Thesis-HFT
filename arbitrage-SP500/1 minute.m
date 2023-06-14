% Load the data
data1 = load('/Users/patrycja_kawalczewska/Desktop/Matlab/SPY_2021/SPY_Tr_20210325.mat');

% Extract the relevant fields
price1 = data1.TAQdata.price;

% Define time and sampling frequency
sampling_freq = 1;
time1 = linspace(datenum('13:29:00'), datenum('13:30:00'), length(price1));

% Create the plot
figure
plot(time1, price1, 'b-', 'LineWidth', 1.5)

% Set axis labels and title
ylabel('SPY Price')
xlabel('Time')
title('SPY Prices from 13:29:00 to 13:30:00')

% Set the format of the x-axis
datetick('x', 'HH:MM:SS', 'keepticks', 'keeplimits')

% Set the color of the grid
grid on
grid minor
set(gca, 'GridColor', 'k', 'GridAlpha', 0.2)

% Add a legend
legend('SPY Price')
