import optuna

def run_algorithm(p1, p2, p3, p4):
    # 假设这是你要调参的传统算法
    return (p1 - 3)**2 + (p2 - 0.5)**2 + (p3 - 0.01)**2 + (p4 + 5) + 0.1

def objective(trial):
    param1 = trial.suggest_int("param1", 1, 10, step=1)
    param2 = trial.suggest_float("param2", 0.0, 1.0, step=0.1)
    param3 = trial.suggest_float("param3", 1e-4, 1e-1, log=True)
    # param4 = trial.suggest_int("param4", -10, 10, step=1)
    param4 = trial.suggest_categorical("param4", [-1, -3, -4, -5])
    error = run_algorithm(param1, param2, param3, param4)
    return error

def main():
    study = optuna.create_study(direction="minimize")
    study.optimize(objective, n_trials=1000)

    print("最优参数：", study.best_params)
    print("最小误差：", study.best_value)


if __name__ == "__main__":
    main()
