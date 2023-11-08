from PyInstaller.utils.hooks import collect_all


datas = []
binaries = []
hiddenimports = ['charset_normalizer.md__mypyc', 'mlflow', 'cartopy']
tmp_ret = collect_all('xgboost')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


block_cipher = None


a = Analysis(
    ['start_cli_pipeline.py',
'cli.py',
'database.py',
'start_dash_pipeline.py',
'_version.py',
'__init__.py',
'./auth/constants.py',
'./auth/dependencies.py',
'./auth/router.py',
'./auth/schemas.py',
'./auth/service.py',
'./auth/sql_models.py',
'./auth/utils.py',
'./auth/__init__.py',
'./data_mining/cli_pipeline.py',
'./data_mining/constants.py',
'./data_mining/dash_pipeline.py',
'./data_mining/router.py',
'./data_mining/schemas.py',
'./data_mining/service.py',
'./data_mining/sql_models.py',
'./data_mining/__init__.py',
'./data_mining/data/inference.py',
'./data_mining/data/data_readiness.py',
'./data_mining/data/feature_engineering.py',
'./data_mining/data/imputation.py',
'./data_mining/data/preprocessing.py',
'./data_mining/data/statistic.py',
'./data_mining/data/__init__.py',
'./data_mining/model/classification.py',
'./data_mining/model/clustering.py',
'./data_mining/model/decomposition.py',
'./data_mining/model/regression.py',
'./data_mining/model/_base.py',
'./data_mining/model/__init__.py',
'./data_mining/model/func/_common_supervised.py',
'./data_mining/model/func/__init__.py',
'./data_mining/model/func/algo_classification/_common.py',
'./data_mining/model/func/algo_classification/_decision_tree.py',
'./data_mining/model/func/algo_classification/_extra_trees.py',
'./data_mining/model/func/algo_classification/_logistic_regression.py',
'./data_mining/model/func/algo_classification/_multi_layer_perceptron.py',
'./data_mining/model/func/algo_classification/_rf.py',
'./data_mining/model/func/algo_classification/_svc.py',
'./data_mining/model/func/algo_classification/_xgboost.py',
'./data_mining/model/func/algo_classification/__init__.py',
'./data_mining/model/func/algo_clustering/_common.py',
'./data_mining/model/func/algo_clustering/_dbscan.py',
'./data_mining/model/func/algo_clustering/_kmeans.py',
'./data_mining/model/func/algo_clustering/__init__.py',
'./data_mining/model/func/algo_decomposition/_common.py',
'./data_mining/model/func/algo_decomposition/_mds.py',
'./data_mining/model/func/algo_decomposition/_pca.py',
'./data_mining/model/func/algo_decomposition/_tsne.py',
'./data_mining/model/func/algo_decomposition/__init__.py',
'./data_mining/model/func/algo_regression/_common.py',
'./data_mining/model/func/algo_regression/_decision_tree.py',
'./data_mining/model/func/algo_regression/_extra_tree.py',
'./data_mining/model/func/algo_regression/_gradient_boosting.py',
'./data_mining/model/func/algo_regression/_knn.py',
'./data_mining/model/func/algo_regression/_lasso_regression.py',
'./data_mining/model/func/algo_regression/_linear_regression.py',
'./data_mining/model/func/algo_regression/_multi_layer_perceptron.py',
'./data_mining/model/func/algo_regression/_polynomial_regression.py',
'./data_mining/model/func/algo_regression/_rf.py',
'./data_mining/model/func/algo_regression/_svr.py',
'./data_mining/model/func/algo_regression/_xgboost.py',
'./data_mining/model/func/algo_regression/__init__.py',
'./data_mining/plot/geochemistry_plot.py',
'./data_mining/plot/map_plot.py',
'./data_mining/plot/statistic_plot.py',
'./data_mining/plot/__init__.py',
'./data_mining/process/classify.py',
'./data_mining/process/cluster.py',
'./data_mining/process/decompose.py',
'./data_mining/process/regress.py',
'./data_mining/process/_base.py',
'./data_mining/process/__init__.py',
'./data_mining/tests/__init__.py',
'./data_mining/tests/test_data/test_data_readiness.py',
'./data_mining/tests/test_data/__init__.py',
'./data_mining/utils/base.py',
'./data_mining/utils/exceptions.py',
'./data_mining/utils/mlflow_utils.py',
'./data_mining/utils/__init__.py',],
    pathex=['C:/Users/DELL/Desktop/gg/geochemistrypi'],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Geochemistry π',
    debug=False,
    strip=False,
    bootloader_ignore_signals=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['logo.png'],
)