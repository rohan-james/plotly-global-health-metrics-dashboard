class ColumnNames:
    def __init__(self, df):
        self.df = df

        self.LIFE_EXPECTANCY_COL = "Life expectancy at birth for both sexes (years)"
        self.FERTILITY_COL = "Total fertility rate (children per women)"
        self.MATERNAL_COL = "Maternal mortality ratio (deaths per 100,000 population)"
        self.UNDER5_COL = (
            "Under five mortality rate for both sexes (per 1,000 live births)"
        )

        self.MALE_LIFE_EXP = "Life expectancy at birth for males (years)"
        self.FEMALE_LIFE_EXP = "Life expectancy at birth for females (years)"

    def find_column(self, df, keywords):
        for col in df.columns:
            col_lower = col.lower()
            for keyword in keywords:
                if keyword.lower() in col_lower:
                    return col
        return None
